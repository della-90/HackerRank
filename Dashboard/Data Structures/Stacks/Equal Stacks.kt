import java.util.*

fun main(args: Array<String>) {
    readLine() // throw away first line

    val s1 = Stack<Int>()
    val s2 = Stack<Int>()
    val s3 = Stack<Int>()

    readLine()!!.split(" ").reversed().map { s1.push(it.toInt()) }
    readLine()!!.split(" ").reversed().map { s2.push(it.toInt()) }
    readLine()!!.split(" ").reversed().map { s3.push(it.toInt()) }

    val stacks = listOf(s1, s2, s3).map { it.sum() }.toMutableList()

    while (stacks.min() != stacks.max()) {
        val highest = stacks.indexOf(stacks.max())
        when (highest) {
            0 -> stacks[0] -= s1.pop()
            1 -> stacks[1] -= s2.pop()
            2 -> stacks[2] -= s3.pop()
        }
    }

    println(stacks[0])
}
