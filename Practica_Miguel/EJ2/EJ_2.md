# ¿Para qué sirve el siguiente programa?¿Qué pasa si el valor es 3?


## Versión MICROBIT
```JS
let valor = 0
valor = Math.randomRange(1, 3)
if (valor == 1) {

basic.showLeds(`
. . # . .
. . # . .
. . # . .
. . # . .
. . # . .
`)

}else if (valor == 2) {
basic.showLeds(`
# . . . #
. # . # .
. . # . .
. # . # .
# . . . #
`)

}
else {

basic.showLeds(`
# # # # #
. . . . #
# # # # #
# . . . .
# # # # #
`)
}

```

## Versión JS WEB
```JS
let boton=document.getElementById("btn")

function ramdonmaker(){
    let valor = Math.floor(Math.random()*4);

    if (valor!=0){
        if (valor == 1){
            console.log("1")
        }else if (valor == 2){
            console.log("X")
        }else{
            console.log("2")
        }
    }
}
boton.addEventListener('click',ramdonmaker)

```