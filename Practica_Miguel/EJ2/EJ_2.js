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

