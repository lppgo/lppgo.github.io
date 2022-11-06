
<div align="center"><font size="35">go zap日志库笔记</font></div>

# 1: 概述

- go zap 高性能日志库;

# 2: 创建实例

- 通过调用 `zap.NewProduction()`/`zap.NewDevelopment()`或者 `zap.Example()`创建一个 Logger。这三个方法的区别在于它将记录的信息不同，参数只能是 string 类型
- 三种创建方式对比：
- Example 和 Production 使用的是 json 格式输出，Development 使用行的形式输出;
- Development:
  - 从警告级别向上打印到堆栈中来跟踪
  - 始终打印包/文件/行（方法）
  - 在行尾添加任何额外字段作为 json 字符串
  - 以大写形式打印级别名称
  - 以毫秒为单位打印 ISO8601 格式的时间戳
- Development
  - 从警告级别向上打印到堆栈中来跟踪
  - 始终打印包/文件/行（方法）
  - 在行尾添加任何额外字段作为 json 字符串
  - 以大写形式打印级别名称
  - 以毫秒为单位打印 ISO8601 格式的时间戳

```go
//代码
var log *zap.Logger
log = zap.NewExample()
log, _ := zap.NewDevelopment()
log, _ := zap.NewProduction()
log.Debug("This is a DEBUG message")
log.Info("This is an INFO message")

//Example 输出
{"level":"debug","msg":"This is a DEBUG message"}
{"level":"info","msg":"This is an INFO message"}

//Development 输出
2018-10-30T17:14:22.459+0800 DEBUG development/main.go:7 This is a DEBUG message
2018-10-30T17:14:22.459+0800 INFO development/main.go:8 This is an INFO message

//Production 输出
{"level":"info","ts":1540891173.3190675,"caller":"production/main.go:8","msg":"This is an INFO message"}
{"level":"info","ts":1540891173.3191047,"caller":"production/main.go:9","msg":"This is an INFO message with fields","region":["us-west"],"id":2}
}
```

# 3: 格式化输出

- zap 有两种类型，分别是**zap.Logger**和**zap.SugaredLogger**,它们惟一的区别是，我们通过调用主 logger 的. Sugar()方法来获取一个 SugaredLogger，然后使用 SugaredLogger 以 printf 格式记录语句，例如:

```go
var sugarLogger *zap.SugaredLogger

func InitLogger() {
logger, _ := zap.NewProduction()
sugarLogger = logger.Sugar()
}

func main() {
InitLogger()
defer sugarLogger.Sync()
sugarLogger.Errorf("Error fetching URL %s : Error = %s", url, err)
}
```

# 4: 写入文件

- 默认情况下日志都会打印到应用程序的 console 界面，但是为了方便查询，可以将日志写入文件，但是我们不能再使用前面创建实例的 3 个方法，而是使用`zap.New()`

```go
package main

import (
	"os"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

var log *zap.Logger

func main() {
	writeSyncer, _ := os.Create("./info.log")         //日志文件存放目录
	encoderConfig := zap.NewProductionEncoderConfig() //指定时间格式
	encoderConfig.EncodeTime = zapcore.ISO8601TimeEncoder
	encoderConfig.EncodeLevel = zapcore.CapitalLevelEncoder
	encoder := zapcore.NewConsoleEncoder(encoderConfig)               //获取编码器,NewJSONEncoder()输出json格式，NewConsoleEncoder()输出普通文本格式
	core := zapcore.NewCore(encoder, writeSyncer, zapcore.DebugLevel) //第三个及之后的参数为写入文件的日志级别,ErrorLevel模式只记录error级别的日志
	log = zap.New(core, zap.AddCaller())                              //AddCaller()为显示文件名和行号
	log.Info("hello world")
	log.Error("hello world")
}


// log输出结果:
2020-12-16T17:53:30.466+0800 INFO geth/main.go:18 hello world
2020-12-16T17:53:30.486+0800 ERROR geth/main.go:19 hello world
```

# 5: 同时输出控制台和文件

- 如果需要同时输出控制台和文件，只需要改造一下 zapcore.NewCore 即可，示例：

```go
package main

import (
	"os"

	"github.com/natefinch/lumberjack"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

var log *zap.Logger

func main() {
	// 获取编码器,NewJSONEncoder()输出json格式，NewConsoleEncoder()输出普通文本格式
	encoderConfig := zap.NewProductionEncoderConfig()
	encoderConfig.EncodeTime = zapcore.ISO8601TimeEncoder //指定时间格式
	encoderConfig.EncodeLevel = zapcore.CapitalLevelEncoder
	encoder := zapcore.NewConsoleEncoder(encoderConfig)

	// 文件writeSyncer
	fileWriteSyncer := zapcore.AddSync(&lumberjack.Logger{
		Filename:   "./info.log", //日志文件存放目录
		MaxSize:    1,            //文件大小限制,单位MB
		MaxBackups: 5,            //最大保留日志文件数量
		MaxAge:     30,           //日志文件保留天数
		Compress:   false,        //是否压缩处理
	})
	fileCore := zapcore.NewCore(encoder, zapcore.NewMultiWriteSyncer(fileWriteSyncer, zapcore.AddSync(os.Stdout)), zapcore.DebugLevel) //第三个及之后的参数为写入文件的日志级别,ErrorLevel模式只记录error级别的日志

	log = zap.New(fileCore, zap.AddCaller()) //AddCaller()为显示文件名和行号

	log.Info("hello world")
	log.Error("hello world")
}
```

# 6: 文件切割

- 日志文件会随时间越来越大，为了避免日志文件把硬盘空间占满，需要按条件对日志文件进行切割，zap 包本身不提供文件切割的功能，但是可以用 zap 官方推荐的`lumberjack`包处理

```go
//文件writeSyncer
fileWriteSyncer := zapcore.AddSync(&lumberjack.Logger{
Filename: "./info.log", //日志文件存放目录，如果文件夹不存在会自动创建
MaxSize: 1, //文件大小限制,单位MB
MaxBackups: 5, //最大保留日志文件数量
MaxAge: 30, //日志文件保留天数
Compress: false, //是否压缩处理
})
```

# 7: 按级别写入文件

- 为了管理人员的查询方便，一般我们需要将低于 error 级别的放到 info.log，error 及以上严重级别日志存放到 error.log 文件中，我们只需要改造一下 zapcore.NewCore 方法的第 3 个参数，然后将文件 WriteSyncer 拆成 info 和 error 两个即可，示例：

```go
package main

import (
	"os"

	"github.com/natefinch/lumberjack"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

var log *zap.Logger

func main() {
	var coreArr []zapcore.Core

	// 获取编码器
	encoderConfig := zap.NewProductionEncoderConfig()            //NewJSONEncoder()输出json格式，NewConsoleEncoder()输出普通文本格式
	encoderConfig.EncodeTime = zapcore.ISO8601TimeEncoder        //指定时间格式
	encoderConfig.EncodeLevel = zapcore.CapitalColorLevelEncoder //按级别显示不同颜色，不需要的话取值zapcore.CapitalLevelEncoder就可以了
	// encoderConfig.EncodeCaller = zapcore.FullCallerEncoder //显示完整文件路径
	encoder := zapcore.NewConsoleEncoder(encoderConfig)

	// 日志级别
	highPriority := zap.LevelEnablerFunc(func(lev zapcore.Level) bool { //error级别
		return lev >= zap.ErrorLevel
	})
	lowPriority := zap.LevelEnablerFunc(func(lev zapcore.Level) bool { //info和debug级别,debug级别是最低的
		return lev < zap.ErrorLevel && lev >= zap.DebugLevel
	})

	// info文件writeSyncer
	infoFileWriteSyncer := zapcore.AddSync(&lumberjack.Logger{
		Filename:   "./log/info.log", //日志文件存放目录，如果文件夹不存在会自动创建
		MaxSize:    1,                //文件大小限制,单位MB
		MaxBackups: 5,                //最大保留日志文件数量
		MaxAge:     30,               //日志文件保留天数
		Compress:   false,            //是否压缩处理
	})
	infoFileCore := zapcore.NewCore(encoder, zapcore.NewMultiWriteSyncer(infoFileWriteSyncer, zapcore.AddSync(os.Stdout)), lowPriority) //第三个及之后的参数为写入文件的日志级别,ErrorLevel模式只记录error级别的日志

	// error文件writeSyncer
	errorFileWriteSyncer := zapcore.AddSync(&lumberjack.Logger{
		Filename:   "./log/error.log", //日志文件存放目录
		MaxSize:    1,                 //文件大小限制,单位MB
		MaxBackups: 5,                 //最大保留日志文件数量
		MaxAge:     30,                //日志文件保留天数
		Compress:   false,             //是否压缩处理
	})
	errorFileCore := zapcore.NewCore(encoder, zapcore.NewMultiWriteSyncer(errorFileWriteSyncer, zapcore.AddSync(os.Stdout)), highPriority) //第三个及之后的参数为写入文件的日志级别,ErrorLevel模式只记录error级别的日志

	coreArr = append(coreArr, infoFileCore)
	coreArr = append(coreArr, errorFileCore)
	log = zap.New(zapcore.NewTee(coreArr...), zap.AddCaller()) //zap.AddCaller()为显示文件名和行号，可省略

	log.Info("hello info")
	log.Debug("hello debug")
	log.Error("hello error")
}
```

- 这样修改之后，info 和 debug 级别的日志就存放到 info.log，error 级别的日志单独放到 error.log 文件中了

# 8: 控制台按级别显示颜色

- 指定编码器的 EncodeLevel 即可

```go
//获取编码器
encoderConfig := zap.NewProductionEncoderConfig() //NewJSONEncoder()输出json格式，NewConsoleEncoder()输出普通文本格式
encoderConfig.EncodeTime = zapcore.ISO8601TimeEncoder //指定时间格式
encoderConfig.EncodeLevel = zapcore.CapitalColorLevelEncoder //按级别显示不同颜色，不需要的话取值zapcore.CapitalLevelEncoder就可以了
encoder := zapcore.NewConsoleEncoder(encoderConfig)
```

# 9: 显示文件路径和行号

- 前面说到要显示文件路径和行号，只需要 zap.New 方法添加参数 zap.AddCaller()即可，如果要显示完整的路径，需要在编码器配置中指定

```go
//获取编码器
encoderConfig := zap.NewProductionEncoderConfig() //NewJSONEncoder()输出json格式，NewConsoleEncoder()输出普通文本格式
encoderConfig.EncodeTime = zapcore.ISO8601TimeEncoder //指定时间格式
encoderConfig.EncodeLevel = zapcore.CapitalColorLevelEncoder //按级别显示不同颜色，不需要的话取值zapcore.CapitalLevelEncoder就可以了
encoderConfig.EncodeCaller = zapcore.FullCallerEncoder //显示完整文件路径
encoder := zapcore.NewConsoleEncoder(encoderConfig)
```

# 10: 完整代码

```go
package main

import (
	"os"

	"github.com/natefinch/lumberjack"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

var log *zap.Logger

func main() {
	var coreArr []zapcore.Core

	// 获取编码器
	encoderConfig := zap.NewProductionEncoderConfig()            //NewJSONEncoder()输出json格式，NewConsoleEncoder()输出普通文本格式
	encoderConfig.EncodeTime = zapcore.ISO8601TimeEncoder        //指定时间格式
	encoderConfig.EncodeLevel = zapcore.CapitalColorLevelEncoder //按级别显示不同颜色，不需要的话取值zapcore.CapitalLevelEncoder就可以了
	// encoderConfig.EncodeCaller = zapcore.FullCallerEncoder //显示完整文件路径
	encoder := zapcore.NewConsoleEncoder(encoderConfig)

	// 日志级别
	highPriority := zap.LevelEnablerFunc(func(lev zapcore.Level) bool { //error级别
		return lev >= zap.ErrorLevel
	})
	lowPriority := zap.LevelEnablerFunc(func(lev zapcore.Level) bool { //info和debug级别,debug级别是最低的
		return lev < zap.ErrorLevel && lev >= zap.DebugLevel
	})

	// info文件writeSyncer
	infoFileWriteSyncer := zapcore.AddSync(&lumberjack.Logger{
		Filename:   "./log/info.log", //日志文件存放目录，如果文件夹不存在会自动创建
		MaxSize:    2,                //文件大小限制,单位MB
		MaxBackups: 100,              //最大保留日志文件数量
		MaxAge:     30,               //日志文件保留天数
		Compress:   false,            //是否压缩处理
	})
	infoFileCore := zapcore.NewCore(encoder, zapcore.NewMultiWriteSyncer(infoFileWriteSyncer, zapcore.AddSync(os.Stdout)), lowPriority) //第三个及之后的参数为写入文件的日志级别,ErrorLevel模式只记录error级别的日志
	// error文件writeSyncer
	errorFileWriteSyncer := zapcore.AddSync(&lumberjack.Logger{
		Filename:   "./log/error.log", //日志文件存放目录
		MaxSize:    1,                 //文件大小限制,单位MB
		MaxBackups: 5,                 //最大保留日志文件数量
		MaxAge:     30,                //日志文件保留天数
		Compress:   false,             //是否压缩处理
	})
	errorFileCore := zapcore.NewCore(encoder, zapcore.NewMultiWriteSyncer(errorFileWriteSyncer, zapcore.AddSync(os.Stdout)), highPriority) //第三个及之后的参数为写入文件的日志级别,ErrorLevel模式只记录error级别的日志

	coreArr = append(coreArr, infoFileCore)
	coreArr = append(coreArr, errorFileCore)
	log = zap.New(zapcore.NewTee(coreArr...), zap.AddCaller()) //zap.AddCaller()为显示文件名和行号，可省略

	log.Info("hello info")
	log.Debug("hello debug")
	log.Error("hello error")
}

```
