import java.util.*

// Complete the bfs function below.
fun bfs(n: Int, m: Int, edges: Array<Array<Int>>, s: Int): Array<Int> {
    val results = Array(n + 1) { -1 }

    val adjacencylist = List(n + 1) {
        mutableSetOf<Int>()
    }

    edges.forEach { (a, b) ->
        adjacencylist[a].add(b)
        adjacencylist[b].add(a)
    }

    var distance = 6
    var toVisit = listOf(s)
    val alreadyVisited = mutableSetOf<Int>()

    while (toVisit.isNotEmpty()) {
        alreadyVisited.addAll(toVisit)
        val neighbours = toVisit
                .flatMap { adjacencylist[it] }
                .filterNot { it in alreadyVisited }

        neighbours.forEach { results[it] = distance }
        toVisit = neighbours
        distance += 6
    }

    return results.sliceArray(1 until s) + results.sliceArray(s + 1..results.lastIndex)
}

private fun findNeighbours(node: Int, matrix: Array<BooleanArray>): List<Int> {
    return matrix[node].withIndex()
            .filter { (_, value) ->
                value
            }
            .map { (index, _) -> index }
}

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)

    val q = scan.nextLine().trim().toInt()

    for (qItr in 1..q) {
        val nm = scan.nextLine().split(" ")

        val n = nm[0].trim().toInt()

        val m = nm[1].trim().toInt()

        val edges = Array<Array<Int>>(m, { Array<Int>(2, { 0 }) })

        for (i in 0 until m) {
            edges[i] = scan.nextLine().split(" ").map { it.trim().toInt() }.toTypedArray()
        }

        val s = scan.nextLine().trim().toInt()

        val result = bfs(n, m, edges, s)

        println(result.joinToString(" "))
    }
}

