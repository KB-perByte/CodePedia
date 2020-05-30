var all []string
var choices = []string{"a", "b", "c"}

func getHappyString(n int, k int) string {
    
    all=make([]string, 0)
    helper(n, "")
    
    if k > len(all){
        return ""
    }
        
    sort.Strings(all)
    return all[k-1]
}


func helper(n int, str string){
    
    if n==0{
        all=append(all, str)
        return 
    }
    
    for i:=0; i< len(choices); i++{
        
        if str=="" || string(str[len(str)-1])!=choices[i]{
            helper(n-1, str+ choices[i])
        }
    }
}