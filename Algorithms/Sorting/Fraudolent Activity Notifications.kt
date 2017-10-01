fun <T : Comparable<T>> List<T>.bisect(value: T, low: Int = 0, high: Int=this.size): Int {
    var _low = low
    var _high = high
    while (_low < _high) {
        val middle = (_high + _low)/2
        if (value > this[middle]) {
            _low = middle+1
        } else {
            _high = middle
        }
    }
    return _low
}

fun <T : Comparable<T>> MutableList<T>.inset(value: T) {
    val index = this.bisect(value)
    this.add(index, value)
}

fun List<Int>.median(): Double {
    if (this.size % 2 != 0) {
        return this[size / 2].toDouble()
    }
    return (this[size / 2 - 1] + this[size / 2]) / 2.0
}

fun main(args: Array<String>) {
    val (n, d) = readLine()!!.split(" ").map { it.toInt() }

    val expenditures: IntArray = readLine()!!.split(" ").map { it.toInt() }.toIntArray()

    var notifications = 0

    val period: MutableList<Int> = expenditures.slice(0 until d).sorted().toMutableList()
    var toRemove = 0
    for (i in (d until n)) {
        val cost = expenditures[i]
        val median = period.median()

        if (cost >= 2 * median) {
            notifications++
        }

        period.removeAt(period.binarySearch(expenditures[toRemove++]))
        period.inset(cost)
    }

    println(notifications)
}
