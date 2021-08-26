
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
        const element = document.getElementById(object.id)
        element.style.backgroundColor = 'green'
    }
}
const playButton = document.getElementById('play-btn')
playButton.addEventListener('click', knapsack)



new Vue({
    el: '#knapsack',
    data() {
        return {
            items: objects,
            walkRight: 0,
            walkLeft: 40,
            direction: 1,
            divPosition: 0,
            speed: 10,
            stepNum: 1,
            queue: [],
            logs: [],
            itemToTake: null,
        }
    },
    mounted() {
        const queue = new PriorityQueue()
        objects.forEach(item => {
            queue.enqueue(item, item.getRatio() * -1)
        })
        while (!queue.isEmpty()) {
            this.queue.push(queue.dequeue().element)
        }
        this.createLog('Using PQueue to get Important treasures')
    },
    watch: {
      direction(value) {
         if (value === -1) {
             this.moveToKnapsack()
         }
      }
    },
    methods: {
        walkSaviour(){
                if (this.walkRight === 60){
                    this.walkRight = 0
                    if (this.direction === 1) {
                        const toTake = this.queue.shift()
                        this.createLog('Saviour arrives to pick item')
                        this.createToTakeItem(toTake)
                        this.turnSaviourLeft()
                        return
                    }
                    this.createLog('Saviour is about to push item into knapsack')
                    this.turnSaviourRight()
                    return
                }
                this.walkRight+=1
                const saviourEl = document.getElementById('saviour')
                saviourEl.style.backgroundPosition =  (-75 * this.stepNum) + "px"
                this.divPosition = this.divPosition + (this.direction * this.speed);
                saviourEl.style.left = this.divPosition + "px"
                this.stepNum = (this.stepNum + 1) % 8;
                setTimeout(this.walkSaviour, 750/this.speed);
        },
        walkSaviourLeft() {
            this.direction = -1
            this.walkSaviour()
        },
        createToTakeItem(item) {
            this.itemToTake = item
            const wrapper = document.getElementById('wrapper')
            const element = document.createElement('div')
            element.style.position = 'absolute'
            element.style.right = '0'
            element.style.bottom = '200px'
            element.id = 'taking ' + item.id
            element.classList.add('box')
            const elementText = document.createElement('p')
            let elementTextNode = document.createTextNode(`Ratio: ${item.getRatio()}`)
            elementText.appendChild(elementTextNode)
            element.appendChild(elementText)
            wrapper.appendChild(element)
            this.createLog('item with '+ item.id +' in view')
        },
        turnSaviourLeft() {
            const saviourEl = document.getElementById('saviour')
            saviourEl.classList.add("facing-left")
            this.createLog('Saviour turns left')
            setTimeout(() => {
                this.walkSaviourLeft()
            }, 500)
        },
        pushItemIntoSack(){
            //TODO the saviour would push item into the sack
            const waterEl = document.getElementById('water')
            const item = document.getElementById('taking ' + this.itemToTake.id)
            console.log(waterEl.clientHeight)
            item.style.display = 'none'
            waterEl.style.height =   ( waterEl.clientHeight + ((this.itemToTake.getRatio() / 15) * 450)) + 'px'
        },
        moveToKnapsack(){
            if (this.direction === 1) {
                this.pushItemIntoSack()
                return
            }
            const item = document.getElementById('taking ' + this.itemToTake.id)
            item.style.left = this.divPosition + "px"
            setTimeout(this.moveToKnapsack, 750/this.speed);

        },
        turnSaviourRight() {
            const saviourEl = document.getElementById('saviour')
            saviourEl.classList.remove("facing-left")
            this.createLog('Saviour turns Right')
            this.direction = 1
            if (this.queue.length) {
                this.walkSaviour()
            }
        },
        createLog(text) {
            setTimeout(() => {
                this.logs.push(text)
            }, 500)
        }
    }
})
