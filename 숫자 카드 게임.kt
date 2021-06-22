class Main() {
  	fun solution(row: Int, column: Int, vararg intArrays: IntArray): Int{
        val cardArray = Array(row){IntArray(column){0}}
        intArrays.forEachIndexed {index, intArray ->
        	cardArray[index] = intArray
        }
        return cardArray.map{intArray ->
        	intArray.reduce{acc,i ->if(acc < i)acc else i}
        }.reduce{acc,pair -> if (acc > pair) acc else pair}
    }
}
fun main(){
    val main = Main()
   	print(main.solution(3,3,intArrayOf(3,1,2),intArrayOf(4,1,4),intArrayOf(2,2,2)))
}
