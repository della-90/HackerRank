import java.util.*

class MaxStack {

    private val stack = Stack<StackItem>()
    private var index = -1

    private class StackItem(val index: Int, val value: Int)

    fun push(value: Int) {
        index++

        if (stack.isEmpty() || value > stack.peek().value) {
            stack.push(StackItem(index, value))
        }
    }

    fun pop() {
        if (!stack.isEmpty() && stack.peek().index == index) {
            stack.pop()
        }
        index--
    }

    fun max(): Int {
        return if (stack.isEmpty()) -1 else stack.peek().value
    }
}


fun main(args: Array<String>) {
    val n = readLine()!!.toInt()
    val stack = MaxStack()
    for (i in 1..n) {
        val components = readLine()!!.split(" ")
        val cmd = components[0].toInt()
        when (cmd) {
            1 -> stack.push(components[1].toInt())
            2 -> stack.pop()
            3 -> println(stack.max())
        }
    }
}
