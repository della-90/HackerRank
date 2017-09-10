import java.io.*
import java.util.*

fun main(args: Array<String>) {
    val lines = readLine()!!.toInt()
    external@ for (i in 0 until lines) {
        val stack = Stack<Char>()
        val line = readLine()!!
        for (char in line) {
            when (char) {
                '{', '[', '(' ->  {
                    stack.push(char)
                }
                '}' -> if (!checkChar(stack, '{')) {
                    println("NO")
                    continue@external
                }
                ']' -> if (!checkChar(stack, '[')) {
                    println("NO")
                    continue@external
                }
                ')' -> if (!checkChar(stack, '(')) {
                    println("NO")
                    continue@external
                }
            }
        }
        println(if (stack.empty()) "YES" else "NO")
    }
}

fun checkChar(stack: Stack<Char>, expected: Char): Boolean {
    return !stack.empty() && stack.pop() == expected
}
