import java.util.*
import kotlin.Comparator

// Complete the quickestWayUp function below.
fun quickestWayUp(ladders: Array<Pair<Int, Int>>, snakes: Array<Pair<Int, Int>>): Int {
    val nodes = List(100) { Node(it + 1, Integer.MAX_VALUE) }
    nodes.first().cost = 0

    val alreadyVisited = mutableSetOf<Node>()
    val toBeVisited = PriorityQueue(Comparator<Node> { x, y -> x.cost.compareTo(y.cost) }.thenByDescending(Node::id))
    toBeVisited.add(nodes.first())

    while (true) {
        val currentNode = toBeVisited.poll()
                ?: return if (nodes.last().cost == Integer.MAX_VALUE) -1 else nodes.last().cost
        alreadyVisited.add(currentNode)

        val neighbours = findNeighbours(currentNode, nodes, ladders, snakes) - alreadyVisited
        neighbours.forEach { neighbour ->
            if (neighbour.cost > currentNode.cost + 1) {
                neighbour.cost = currentNode.cost + 1
                neighbour.previous = currentNode
            }
        }

        toBeVisited.addAll(neighbours)
    }
}

private fun findNeighbours(currentPosition: Node, nodes: List<Node>, ladders: Array<Pair<Int, Int>>, snakes: Array<Pair<Int, Int>>): List<Node> {
    val boardCellNumber = currentPosition.id + 1..currentPosition.id + 6
    val nextPositions = boardCellNumber.map { id ->
        // check if there's any corresponding ladder or snake
        ladders.find { (start, _) -> start == id }?.second ?: snakes.find { (start, _) -> start == id }?.second ?: id
    }

    return nodes.filter { it.id in nextPositions }
}

data class Node(val id: Int, var cost: Int, var previous: Node? = null)

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)

    val t = scan.nextInt()

    repeat(t) {
        val n = scan.nextInt()

        val ladders = Array(n) {
            Pair(scan.nextInt(), scan.nextInt())
        }

        val m = scan.nextInt()

        val snakes = Array(m) {
            Pair(scan.nextInt(), scan.nextInt())
        }

        val result = quickestWayUp(ladders, snakes)

        println(result)
    }
}

