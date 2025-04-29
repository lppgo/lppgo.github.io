
<div align='center' ><font size='50'>Golang Files and I/O</font></div>

<!-- [toc] -->

# Table of Contents

- [Table of Contents](#table-of-contents)
- [一：读文件](#一读文件)
  - [1.1 读一个 whole 文件](#11-读一个-whole-文件)
  - [1.2 读一个文件，close](#12-读一个文件close)
  - [1.3 read file by line](#13-read-file-by-line)
- [二：写文件](#二写文件)
  - [2.1 Write the whole file](#21-write-the-whole-file)
  - [2.2 Open file for writing](#22-open-file-for-writing)
  - [2.3 Open file for appending](#23-open-file-for-appending)
  - [2.4 Write to a file](#24-write-to-a-file)
  - [2.5 File permissions when creating files](#25-file-permissions-when-creating-files)
- [三：File Operations](#三file-operations)
  - [3.1 获取文件 size](#31-获取文件-size)
  - [3.2 获取文件 information](#32-获取文件-information)
  - [3.3 检查文件是否 Exist](#33-检查文件是否-exist)
  - [3.4 Delete File](#34-delete-file)
  - [3.5 Rename File](#35-rename-file)
  - [3.6 Copy a File](#36-copy-a-file)
- [四：目录相关操作 Directory Operations](#四目录相关操作-directory-operations)
  - [4.1 Create directory](#41-create-directory)
  - [4.2 Remove Directory](#42-remove-directory)
  - [4.3 列出目录下面的文件 List files in a directory](#43-列出目录下面的文件-list-files-in-a-directory)
  - [4.4 Recursive 递归的 List 文件](#44-recursive-递归的-list-文件)
- [五：File Path Operations](#五file-path-operations)
  - [5.1 Join a path](#51-join-a-path)
  - [5.2 Split a path into a directory and file](#52-split-a-path-into-a-directory-and-file)
  - [5.3 Split list of paths](#53-split-list-of-paths)
  - [5.4 Get file name from path](#54-get-file-name-from-path)
  - [5.5 Get directory name from path](#55-get-directory-name-from-path)
  - [5.6 获取文件拓展名 Get file extension](#56-获取文件拓展名-get-file-extension)
- [六：IO related interface](#六io-related-interface)
  - [6.1 io.Reader](#61-ioreader)
  - [6.2 io.Writer](#62-iowriter)
  - [6.3 io.Closer](#63-iocloser)
  - [6.4 io.ReaderAt](#64-ioreaderat)
  - [6.5 io.WriterAt](#65-iowriterat)
  - [6.6 io.Seeker](#66-ioseeker)

# 一：读文件

## 1.1 读一个 whole 文件

```go
d, err := ioutil.ReadFile("foo.txt")
if err != nil {
    log.Fatalf("ioutil.ReadFile failed with '%s'\n", err)
}
fmt.Printf("Size of 'foo.txt': %d bytes\n", len(d))
```

## 1.2 读一个文件，close

```go
f, err := os.Open("foo.txt")
if err != nil {
    log.Fatalf("os.Open failed with '%s'\n", err)
}
defer f.Close()
```

## 1.3 read file by line

```go
// ReadLines reads all lines from a file
func ReadLines(filePath string) ([]string, error) {
	file, err := os.OpenFile(filePath, os.O_RDONLY, 0644)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	res := make([]string, 0)
	for scanner.Scan() {
		line := scanner.Text()
		res = append(res, line)
	}
	if err = scanner.Err(); err != nil {
		return nil, err
	}
	return res, nil
}

func main() {
	path := "main.go"
	lines, err := ReadLines(path)
	if err != nil {
		log.Fatalf("ReadLines failed with '%s'\n", err)
	}
	fmt.Printf("File %s has %d lines\n", path, len(lines))
}
```

# 二：写文件

## 2.1 Write the whole file

```go
d := []byte("content of the file")
err := ioutil.WriteFile("foo.txt", d, 0644)
if err != nil {
    log.Fatalf("ioutil.WriteFile failed with '%s'\n", err)
}
```

## 2.2 Open file for writing

```go
f, err := os.Create("foo.txt")
if err != nil {
    log.Fatalf("os.Open failed with '%s'\n", err)
}
```

## 2.3 Open file for appending

```go
f, err := os.OpenFile(filePath, os.O_WRONLY | os.O_APPEND | os.O_CREATE, 0666)
if err != nil {
    log.Fatalf("os.Open failed with '%s'\n", err)
}
```

## 2.4 Write to a file

```go
d := []byte("data to write")
nWritten, err := f.Write(d)
```

## 2.5 File permissions when creating files

使用 os.Create 或创建新文件时 os.OpenFile，需要为新文件提供文件权限。

对于大多数情况 **0644** 是一个不错的选择。

这些是八进制格式的 Unix 样式权限。

# 三：File Operations

## 3.1 获取文件 size

```go
func GetFileSize(path string) (int64, error) {
	st, err := os.Lstat(path)
	if err != nil {
		return -1, err
	}
	return st.Size(), nil
}
```

## 3.2 获取文件 information

```go
	st, err := os.Stat("main.go")
	if err != nil {
		log.Fatalf("GetFileSize failed with '%s'\n", err)
	}
	fmt.Printf(`Name: %s
Size: %d
IsDir: %v
Mode: %x
ModTime: %s
OS info: %#v
`, st.Name(), st.Size(), st.IsDir(), st.Mode, st.ModTime(), st.Sys())
```

## 3.3 检查文件是否 Exist

```go
func IsPathExists(path string) (bool, error) {
	_, err := os.Lstat(path)
	if err == nil {
		return true, nil
	}
	if os.IsNotExist(err) {
		return false, nil
	}
	// error other than not existing e.g. permission denied
	return false, err
}
```

## 3.4 Delete File

```go
path := "foo.txt"
err := os.Remove(path)
if err != nil {
    if os.IsNotExist(err) {
        fmt.Printf("os.Remove failed because file doesn't exist\n")
    } else {
        fmt.Printf("os.Remove failed with '%s'\n", err)
    }
}
```

## 3.5 Rename File

```go
oldPath := "old_name.txt"
newPath := "new_name.txt"
err := os.Rename(oldPath, newPath)
if err != nil {
    fmt.Printf("os.Rename failed with '%s'\n", err)
}
```

## 3.6 Copy a File

```go
// CopyFile copies a src file to dst
func CopyFile(dst, src string) error {
	srcFile, err := os.Open(src)
	if err != nil {
		return err
	}
	defer srcFile.Close()

	dstFile, err := os.Create(dst)
	if err != nil {
		return err
	}
	_, err = io.Copy(dstFile, srcFile)
	err2 := dstFile.Close()
	if err == nil && err2 != nil {
		err = err2
	}
	if err != nil {
		// delete the destination if copy failed
		os.Remove(dst)
	}
	return err
}
```

# 四：目录相关操作 Directory Operations

## 4.1 Create directory

```go
dir := "my_dir"
err := os.Mkdir(dir, 0755)
if err != nil {
    fmt.Printf("os.Mkdir('%s') failed with '%s'\n", dir)
}
dir := filepath.Join("topdir", "subdir")
err := os.MkdirAll(dir, 0755)
if err != nil {
    fmt.Printf("os.MkdirAll('%s') failed with '%s'\n", dir)
}
```

- `os.Mkdir` only succeeds if parent directory of dir already exists.

- `os.MkdirAll` will create all intermediary directories.

- `0755` describes permissions for the directory.

## 4.2 Remove Directory

- `os.Remove` only works for empty directories i.e. directories without any files of sub-directories.
  ```go
  dir := "my_dir"
  err := os.Remove(dir)
  if err != nil {
    fmt.Printf("os.Remove('%s') failed with '%s'\n", path, err)
  }
  ```
- `os.RemoveAll` removes the directory and all its children (files and sub-directories).
  ```go
  dir := "my_dir"
  err := os.RemoveAll(dir)
  if err != nil {
    fmt.Printf("os.RemoveAll('%s') failed with '%s'\n", path, err)
  }
  ```

## 4.3 列出目录下面的文件 List files in a directory

```go
func main() {
	dir := "."
	fileInfos, err := ioutil.ReadDir(dir)
	if err != nil {
		log.Fatalf("ioutil.ReadDir('%s') failed with '%s'\n", dir, err)
	}
	for _, fi := range fileInfos {
		fmt.Printf("Path: %s, is dir: %v, size: %d bytes\n", fi.Name(), fi.IsDir(), fi.Size())
	}
}
```

## 4.4 Recursive 递归的 List 文件

```go
// 递归获取指定目录下的所有文件名
func GetAllFile(pathname string) ([]string, error) {
	result := []string{}

	fis, err := ioutil.ReadDir(pathname)
	if err != nil {
		fmt.Printf("读取文件目录失败，pathname=%v, err=%v \n",pathname, err)
		return result, err
	}

	// 所有文件/文件夹
	for _, fi := range fis {
		fullname := pathname + "/" + fi.Name()
		// 是文件夹则递归进入获取;是文件，则压入数组
		if fi.IsDir() {
			temp, err := GetAllFile(fullname)
			if err != nil {
				fmt.Printf("读取文件目录失败,fullname=%v, err=%v",fullname, err)
				return result, err
			}
			result = append(result, temp...)
		} else {
			result = append(result, fullname)
		}
	}

	return result, nil

```

# 五：File Path Operations

## 5.1 Join a path

```go
path := filepath.Join("dir", "sub", "file.txt")
fmt.Printf("path: %s\n", path)

// path: dir/sub/file.txt
```

## 5.2 Split a path into a directory and file

```go
path := filepath.Join("dir", "file.txt")
file := filepath.Base(path)
fmt.Printf("path: %s, file: %s\n", path, file)

// path: dir/file.txt, file: file.txt
```

## 5.3 Split list of paths

```go
parts := filepath.SplitList("/usr/bin:/tmp")
fmt.Printf("parts: %#v\n", parts)

// parts: []string{"/usr/bin", "/tmp"}
```

## 5.4 Get file name from path

```go
path := filepath.Join("dir", "file.txt")
dir, file := filepath.Split(path)
fmt.Printf("dir: %s, file: %s\n", dir, file)

// dir: dir/, file: file.txt
```

## 5.5 Get directory name from path

```go
path := filepath.Join("dir", "file.txt")
dir := filepath.Dir(path)
fmt.Printf("path: %s, dif: %s\n", path, dir)

// path: dir/file.txt, dif: dir
```

## 5.6 获取文件拓展名 Get file extension

```go
ext := filepath.Ext("file.txt")
fmt.Printf("ext: %s\n", ext)

// ext: .txt
```

# 六：IO related interface

## 6.1 io.Reader

- `io.Reader` 是读取顺序字节流的关键的抽象；
- `Read`函数将最多 len(p) byte 读入一个 buffer 缓冲区 p，返回一个读取的字节和错误的状态；
- 当它到达文件结尾的时候，返回一个`io.EOF`错误
- `io.Reader`不允许返回流中。为此，类型必须实现`io.Seeker`或`io.ReaderAt`接口;

```go
type  Reader  interface  {
    Read (p [] byte)  (n  int ,  err  error)
}
```

## 6.2 io.Writer

- `io.Writer`用于写入顺序的字节流 bytes stream;
- `Write` writes bytes in `p` and returns the number of bytes written and error status.
- Write 保证它会写入所有数据或返回错误，即如果返回的 n 是 < len(p) 则 err 必须非零;
  ```go
  type Writer interface{
      Write (p []byte) (n int,err error)
  }
  ```

## 6.3 io.Closer

- Closer describes streams that must be explicitly closed.(Closer 描述必须显式的 close 的流)；
- Close returns an error because it’s required in some real-world cases. For example, 在对文件进行缓冲写入时，Close 可能需要将剩余的缓冲数据刷新到文件中，这可能会失败.

```go
type  Closer  interface  {
        Close ()  error
}
```

## 6.4 io.ReaderAt

- io.ReaderAt is like io.Reader but allows to read at any position in the stream.

```go
type ReaderAt interface {
        ReadAt(p []byte, off int64) (n int, err error)
}
```

## 6.5 io.WriterAt

- io.WriterAt is like io.Write but allows to write at an arbitrary position in the stream.
  ```go
  type WriterAt interface {
        WriteAt(p []byte, off int64) (n int, err error)
  }
  ```

## 6.6 io.Seeker

- io.Seeker allows seeking within the stream. If you can seek, you can also implement io.ReaderAt and io.WriterAt.

```go
type Seeker interface {
        Seek(offset int64, whence int) (int64, error)
}
```
