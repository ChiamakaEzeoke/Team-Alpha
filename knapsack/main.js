
class QueueElement {
    constructor(element, priority)
    {
        this.element = element;
        this.priority = priority;
    }
}
 
class PriorityQueue {
    constructor() {
        this.items = [];
    }
    enqueue(element, priority) {
        let queueElement = new QueueElement(element, priority);
        let contain = false;
        for (let i = 0; i < this.items.length; i++) {
            if (this.items[i].priority > queueElement.priority) {
                this.items.splice(i, 0, queueElement);
                contain = true;
                break;
            }
        }
        if (!contain) {
            this.items.push(queueElement);
        }
    }
    dequeue() {
        if (this.isEmpty())
            return "Underflow";
        return this.items.shift();
    }
    isEmpty() {
        return this.items.length == 0;
    }
    printPQueue() {
        let str = "";
        for (let i = 0; i < this.items.length; i++)
            str += this.items[i].element + " ";
        return str;
    }
}
class Item{
    constructor(id, profit, weight) {
        this.id = id
        this.profit = profit;
        this.weight = weight;
    }

    toString() {
        return `Id: ${this.id}, Profit: ${this.profit}, Weight: ${this.weight}`
    }

    getRatio() {
        return Number(this.profit /this.weight).toFixed(2)
    }

    toObject() {
        return {
            id: this.id,
            profit: this.profit,
            weight: this.weight
        }
    }

    setWeight(newWeight) {
        this.weight = newWeight
    } 

    setProfit(newWeight) {
        this.profit = this.profit * (newWeight/this.weight)
    }
}

const objects = [
    new Item('A', 5, 1),
    new Item('B', 10, 3),
    new Item('C', 15, 5),
    new Item('D', 7, 4  ),
    new Item('E', 8, 1),
    new Item('F', 9, 3),
    new Item('G', 4, 2),
]

const items = document.getElementById('items')
objects.forEach(item => {
    const element = document.createElement('div')
    element.id = item.id
    element.classList.add('box')
    const elementText = document.createElement('p')
    elementTextNode = document.createTextNode(`Ratio: ${item.getRatio()}`)
    elementText.appendChild(elementTextNode)
    element.appendChild(elementText)
    items.appendChild(element)
})
const knapsack = async () => {
    let capacity = 15
    const timer = ms => new Promise(res => setTimeout(res, ms))
    const queue = new PriorityQueue()
    objects.forEach(item => {
        queue.enqueue(item, item.getRatio() * -1)
    }) 
    const profits = []
    let totalProfits = 0
    while (capacity != 0 && !queue.isEmpty()) {
        const mostWeighted = queue.dequeue()
        if (capacity < mostWeighted.element.weight) {
            mostWeighted.element.setProfit(capacity)
            mostWeighted.element.setWeight(capacity)
        }
        capacity -= mostWeighted.element.weight
        profits.push(mostWeighted)
        updateUI(mostWeighted.element)
        totalProfits+= mostWeighted.element.profit
        await timer(2500); // then t
    }
    function updateUI(object) {
        console.log(object)
        const element = document.getElementById(object.id)
        element.style.backgroundColor = 'green'
    }
}
const playButton = document.getElementById('play-btn')
playButton.addEventListener('click', knapsack)