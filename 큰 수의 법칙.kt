fun main(args: Array<String>) {
  	val n = 7
  	val m = 14
  	val k = 4
  	val data = listOf<Int>(1,2,3,4,5,6,7).sortedBy{-it}
	
    var first = data[0]
    var second = data[1]
    
    val count = ((m/(k+1)*k) + (m%(k+1)))
    
    var result = 0
   	result += ((count) * first)
    result += (m - count) * second
    
    print(result)
}
