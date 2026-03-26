
<div align="center"><font size="35">Go 结构体验证神器validator</font></div>

# 1: 概述

- 在 Web 服务、RPC 接口、配置加载这类场景里，我们经常要对输入数据做合法性校验；
- 如果完全手写 `if/else` 或正则，一个字段一个字段判断，代码很快就会变得又长又散；
- `github.com/go-playground/validator/v10` 是 Go 里非常经典的结构体校验库，支持通过 tag 对字段、结构体、切片、map 甚至跨字段关系做验证；
- gin 默认就集成了这套验证能力，所以很多 Go Web 项目其实早就在间接使用它；
- 原文参考: `https://mp.weixin.qq.com/s/Ycs22tC45BjrjnefRBtDnA`

- `validator` 的核心价值，不只是“少写几行判断”，而是把约束直接贴在数据结构上。这样一眼看结构体，就能知道这个模型的业务边界，也更容易避免脏数据一路流到服务内部。

# 2: 安装

```go
go get github.com/go-playground/validator/v10
```

```go
import "github.com/go-playground/validator/v10"
```

- 新项目建议直接使用 `v10` 版本；
- 官方文档里也建议尽量复用同一个 `Validate` 实例，因为内部会缓存结构体元信息，重复创建没有必要。

# 3: 最简单的例子

```go
package main

import (
    "fmt"

    "github.com/go-playground/validator/v10"
)

type User struct {
    Name string `validate:"min=6,max=10"`
    Age  int    `validate:"min=1,max=100"`
}

func main() {
    validate := validator.New()

    u1 := User{Name: "lidajun", Age: 18}
    fmt.Println(validate.Struct(u1))

    u2 := User{Name: "dj", Age: 101}
    fmt.Println(validate.Struct(u2))
}
```

- 上面这个例子里，`Name` 被要求长度在 `6~10` 之间，`Age` 被要求在 `1~100` 之间；
- `validate.Struct(u1)` 校验通过时返回 `nil`；
- 一旦校验失败，会返回包含字段名和 tag 信息的错误。

```go
<nil>
Key: 'User.Name' Error:Field validation for 'Name' failed on the 'min' tag
Key: 'User.Age' Error:Field validation for 'Age' failed on the 'max' tag
```

- 这类错误信息比单纯返回 `false` 实用得多，因为你能直接看出来到底是哪个字段违反了哪个规则；
- 结构体越复杂、规则越多，`validator` 的收益就越明显。

# 4: 基本使用步骤

- 使用 `validator` 做结构体校验，通常就 3 步：
  - 创建校验器：`validate := validator.New()`;
  - 定义带 `validate` tag 的结构体；
  - 调用 `validate.Struct(obj)` 执行校验；
- 如果只想校验单个变量，也可以用 `validate.Var(value, rule)`。

```go
package main

import (
    "fmt"

    "github.com/go-playground/validator/v10"
)

func main() {
    validate := validator.New()

    email := "joeybloggs.gmail.com"
    err := validate.Var(email, "required,email")
    fmt.Println(err)
}
```

- `Var()` 比较适合校验单个字符串、单个参数、配置项；
- `Struct()` 更适合接口入参、表单对象、配置对象这类完整模型；
- 一般在业务里最常见的还是 `Struct()`。

# 5: 常见 tag 怎么看

- `validator` 的规则全部写在 `validate:"..."` 里；
- 同一个字段可以组合多个规则：
  - `,` 表示“并且”；
  - `|` 表示“或者”；
- 常见示例：

```go
type SignUp struct {
    Username string `validate:"required,min=4,max=20"`
    Password string `validate:"required,min=8"`
    Email    string `validate:"required,email"`
    Age      uint8  `validate:"gte=0,lte=130"`
    Role     string `validate:"oneof=admin user guest"`
}
```

- 这里面最常见的几个规则如下：
  - `required`：不能为空，也不能是类型默认值；
  - `min` / `max`：字符串是长度限制，数字是范围限制；
  - `gte` / `lte`：大于等于、小于等于；
  - `oneof`：枚举值之一；
  - `email` / `url` / `ip`：格式校验。

- 一个容易忽略的细节是：tag 之间不要插空格，例如 `validate:"required, email"` 这种写法是有风险的，实际项目里应始终紧凑书写。

# 6: 结构体校验示例

```go
package main

import (
    "fmt"

    "github.com/go-playground/validator/v10"
)

type Address struct {
    Street string `validate:"required"`
    City   string `validate:"required"`
    Planet string `validate:"required"`
    Phone  string `validate:"required"`
}

type User struct {
    FirstName      string     `validate:"required"`
    LastName       string     `validate:"required"`
    Age            uint8      `validate:"gte=0,lte=130"`
    Email          string     `validate:"required,email"`
    FavouriteColor string     `validate:"iscolor"`
    Addresses      []*Address `validate:"required,dive,required"`
}

func main() {
    validate := validator.New()

    address := &Address{
        Street: "Eavesdown Docks",
        Planet: "Persphone",
        Phone:  "none",
    }

    user := &User{
        FirstName:      "Badger",
        LastName:       "Smith",
        Age:            135,
        Email:          "Badger.Smith@gmail.com",
        FavouriteColor: "#000-",
        Addresses:      []*Address{address},
    }

    err := validate.Struct(user)
    fmt.Println(err)
}
```

- 这个例子里故意留了几个错误：
  - `Age=135` 超过了 `lte=130`;
  - `FavouriteColor="#000-"` 不是合法颜色；
  - `Address.City` 没填，违反 `required`。

- 这也是 `validator` 很适合接口层的原因：一旦请求模型不合法，就能在很靠前的位置拦住，而不是等业务逻辑运行一半才报错。

# 7: dive 是什么

- `dive` 是 `validator` 非常好用的一个能力；
- 它的意思是：当前字段如果是 `slice`、`array`、`map` 这类容器，不要停在外层，继续往内部元素做校验。

```go
package main

import (
    "fmt"

    "github.com/go-playground/validator/v10"
)

func main() {
    validate := validator.New()

    slice := []string{"123", "onetwothree", "myslicetest", "four", "five"}
    err := validate.Var(slice, "max=15,dive,min=4")
    fmt.Println(err)
}
```

- `max=15` 作用在整个切片；
- `dive` 后面的 `min=4` 作用在切片里的每一个元素；
- 也就是说，`dive` 之后的规则，是“向里一层”再应用。

- 如果是二维切片，也可以连续使用多个 `dive`：

```go
validate.Var(data, "min=2,dive,len=2,dive,required")
```

- 记忆方式很简单：每出现一次 `dive`，就继续往里走一层。

# 8: map 和跨字段校验

- 对 `map` 做校验时，除了 `dive`，还可以结合 `keys` 和 `endkeys` 校验 key；
- 对注册表单这种场景，还经常会用到跨字段比较。

```go
type RegisterUser struct {
    UserName  string `validate:"gte=4,lte=14"`
    Password  string `validate:"min=6,max=20"`
    Password2 string `validate:"eqfield=Password"`
}
```

- `eqfield=Password` 表示 `Password2` 必须等于 `Password`；
- 这个场景最典型的用途就是“重复输入密码”校验；
- 其他类似规则还有：
  - `nefield`：不能等于另一个字段；
  - `gtefield` / `ltefield`：与同结构体字段比较大小；
  - `eqcsfield`：跨嵌套结构体字段比较。

- 这些能力能让很多“字段之间有关系”的校验直接声明在 tag 里，减少散落在 handler 里的判断代码。

# 9: 自定义校验

- 内置 tag 虽然很多，但总有一些业务规则比较个性化；
- 这时可以通过 `RegisterValidation()` 注册自定义规则。

```go
package main

import (
    "fmt"

    "github.com/go-playground/validator/v10"
)

type User struct {
    Name string `validate:"required,CustomerValidation"`
    Age  uint8  `validate:"gte=0,lte=80"`
}

var validate *validator.Validate

func main() {
    validate = validator.New()
    validate.RegisterValidation("CustomerValidation", CustomerValidationFunc)

    user := &User{Name: "tom", Age: 29}
    err := validate.Struct(user)
    fmt.Println(err)
}

func CustomerValidationFunc(fl validator.FieldLevel) bool {
    return fl.Field().String() == "jimmy"
}
```

- 上面的逻辑表示 `Name` 必须等于 `jimmy`；
- 当然，这只是为了演示自定义校验的写法，真实业务里你可以把它替换成手机号前缀、业务编号格式、日期区间等自己的规则；
- 如果业务逻辑已经复杂到“单个字段的 tag 表达不清”，也可以使用结构体级别校验。

# 10: 错误处理

- 很多人第一次用 `validator` 时，都是直接 `fmt.Println(err)`；
- 这在开发期够用，但线上一般还要把错误翻译成用户可读信息、日志字段或者错误码；
- 这时就需要把返回的 `error` 断言成 `validator.ValidationErrors`。

```go
err := validate.Struct(user)
if err != nil {
    if _, ok := err.(*validator.InvalidValidationError); ok {
        fmt.Println(err)
        return
    }

    for _, fieldErr := range err.(validator.ValidationErrors) {
        fmt.Println("Namespace:", fieldErr.Namespace())
        fmt.Println("Field:", fieldErr.Field())
        fmt.Println("Tag:", fieldErr.Tag())
        fmt.Println("ActualTag:", fieldErr.ActualTag())
        fmt.Println("Value:", fieldErr.Value())
        fmt.Println("Param:", fieldErr.Param())
    }
}
```

- 常用的几个字段：
  - `Field()`：字段名；
  - `Tag()`：失败的校验规则；
  - `ActualTag()`：真实规则，别名场景尤其有用；
  - `Value()`：当前值；
  - `Param()`：规则参数，例如 `130`、`20` 这种；
- 有了这些信息，就能自己拼装中文错误提示，或者对接国际化翻译器。

# 11: 在 Web 项目里的使用建议

- `validator` 最适合放在“请求进入业务之前”的那一层；
- 常见落点包括：
  - HTTP handler 参数绑定后；
  - RPC 请求对象进入 service 前；
  - 配置文件加载完成后；
  - 定时任务参数解析后；
- 如果你在用 gin，很多场景下已经默认走了这套机制，只需要把规则写在结构体 tag 上。

```go
type CreateUserReq struct {
    Name     string `json:"name" validate:"required,min=2,max=20"`
    Email    string `json:"email" validate:"required,email"`
    Password string `json:"password" validate:"required,min=8"`
}
```

- 这种做法的好处是：
  - 参数约束集中在模型定义上；
  - handler 更干净；
  - 错误处理更统一；
  - 模型本身的可读性更强。

# 12: 小结

- `validator` 是 Go 项目里非常值得掌握的一类基础库；
- 它最核心的能力是通过 tag 把约束贴到结构体上，让校验逻辑声明化；
- 对简单场景，`required`、`min/max`、`email` 这些内置 tag 已经足够实用；
- 对复杂场景，还可以用 `dive`、跨字段比较、自定义校验、错误翻译来继续扩展；
- 如果你的接口模型越来越多、规则越来越复杂，尽早把 `validator` 用起来，通常比在业务代码里到处手写校验更稳、更清晰。

# 13: 参考

- 官方仓库: `https://github.com/go-playground/validator`
- 文档: `https://pkg.go.dev/github.com/go-playground/validator/v10`
- 原文参考: `https://mp.weixin.qq.com/s/Ycs22tC45BjrjnefRBtDnA`
