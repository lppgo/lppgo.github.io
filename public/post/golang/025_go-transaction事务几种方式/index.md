
<div align="center"><font size="35">Go-transaction事务几种方式</font></div>

# 1：方式一

- 这种写法非常朴实，程序流程也非常明确，但是事务处理与程序流程嵌入太深，容易遗漏，造成严重的问题

```go
func DoSomething() (err error) {
    tx, err := db.Begin()
    if err != nil {
        return
    }


    defer func() {
        if p := recover(); p != nil {
            tx.Rollback()
            panic(p)  // re-throw panic after Rollback
        }
    }()


    if _, err = tx.Exec(...); err != nil {
        tx.Rollback()
        return
    }
    if _, err = tx.Exec(...); err != nil {
        tx.Rollback()
        return
    }
    // ...


    err = tx.Commit()
    return
}
```

# 2: 方式二

- 下面这种写法把事务处理从程序流程抽离了出来，不容易遗漏，但是作用域是整个函数，程序流程不是很清晰

```go
func DoSomething() (err error) {
    tx, err := db.Begin()
    if err != nil {
        return
    }


    defer func() {
        if p := recover(); p != nil {
            tx.Rollback()
            panic(p) // re-throw panic after Rollback
        } else if err != nil {
            tx.Rollback()
        } else {
            err = tx.Commit()
        }
    }()


    if _, err = tx.Exec(...); err != nil {
        return
    }
    if _, err = tx.Exec(...); err != nil {
        return
    }
    // ...
    return
}

```

# 3: 方式三

- 写法三是对写法二的进一步封装，写法高级一点，缺点同上

```go
func Transact(db *sql.DB, txFunc func(*sql.Tx) error) (err error) {
    tx, err := db.Begin()
    if err != nil {
        return
    }


    defer func() {
        if p := recover(); p != nil {
            tx.Rollback()
            panic(p) // re-throw panic after Rollback
        } else if err != nil {
            tx.Rollback()
        } else {
            err = tx.Commit()
        }
    }()


    err = txFunc(tx)
    return err
}


func DoSomething() error {
    return Transact(db, func (tx *sql.Tx) error {
        if _, err := tx.Exec(...); err != nil {
            return err
        }
        if _, err := tx.Exec(...); err != nil {
            return err
        }
    })
}
```
