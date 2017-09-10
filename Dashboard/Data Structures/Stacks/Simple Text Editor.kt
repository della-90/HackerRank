import java.util.*

var builder = StringBuilder()
val tmpStrings = Stack<String>()

fun main(args: Array<String>) {
    val lines = readLine()!!.toInt()
    for (i in 1..lines) {
        val line = readLine()!!.split(" ")
        val cmd = line[0].toInt()

        when (cmd) {
            1 -> append(line[1])
            2 -> delete(line[1].toInt())
            3 -> printChar(line[1].toInt())
            4 -> undo()
        }
    }
}

fun append(s: String) {
    tmpStrings.push(builder.toString())
    builder.append(s)
}

fun delete(n: Int) {
    tmpStrings.push(builder.toString())
    builder.setLength(builder.length - n)
}

fun printChar(n: Int) {
    println(builder.toString()[n-1])
}

fun undo() {
    builder = StringBuilder(tmpStrings.pop())
}
