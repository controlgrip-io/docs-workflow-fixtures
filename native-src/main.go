package main
import("fmt";"io";"os")
func main(){ _, _ = io.ReadAll(os.Stdin); fmt.Println(`{"stream":"users","data":{"id":1,"runtime":"golang"}}`) }
