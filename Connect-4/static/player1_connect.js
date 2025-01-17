
reloaded = false


function autoUpdate() {
    myVar = setInterval(getNewBoard, 500);
}

function getNewBoard(){
    const Http =  new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/autoUpdate"
    Http.open("GET",url)
    Http.send()
    Http.onload = function(){
        if(Http.readyState == Http.DONE){
            if(Http.status == 200){
                data = JSON.parse(Http.response)
                
                if(data['move'] != ""){

                    turn = data['color']
                    if(turn != "" && !reloaded){
                        try{
                            btns = document.getElementsByClassName("options")
                            btns[0].style.display = 'none'
                            btns[1].style.display =  'none'
                        }
                        finally{
                            reloaded = true
                        }
                    }

                    displayBoard(data['move'])
                    if(data['winner'].length > 0){
                        document.getElementById('mstatus').innerHTML = data['winner'].charAt(0).toUpperCase()+ data['winner'].slice(1) + " Wins!"
                        showResetButton()
                    }else{
                        console.log(data)
                        if(data['color']!=''){
                            if(data['col'] == null && document.getElementById('mstatus').innerHTML == "Please Wait for Opponent to Make Move"){
                                document.getElementById('status').innerHTML = ""
                            }
                            if(data['col'] == null){
                                document.getElementById('mstatus').innerHTML = data['color'].charAt(0).toUpperCase() + data['color'].slice(1)+": Please Make Move"
                            }
                        }
                    }

                }

            }
        }
    }
}

function printVals(){
    console.log(player2_color)
    console.log(player1_color)
    console.log(current_turn)
}

function pickRed(){
    const Http =  new XMLHttpRequest();
    const url = 'http://127.0.0.1:5000/p1Color?color=red'
    window.location.href = url

    btns = document.getElementsByClassName("options")
    btns[0].style.display = 'none'
    btns[1].style.display =  'none'
    reloaded = true
    
    
}

function pickYellow(){
    const Http =  new XMLHttpRequest();
    const url = 'http://127.0.0.1:5000/p1Color?color=yellow'
    window.location.href = url
    btns = document.getElementsByClassName("options")
    btns[0].style.display = 'none'
    btns[1].style.display =  'none'
    reloaded = true
    
}

function displayBoard(board){
    for(var row = 0; row < board.length; row++){
        for(var col = 0; col < board[0].length; col++){
            if(board[row][col] == 'red'){
                document.getElementsByClassName('col'+ (col+1))[row].style.backgroundColor = 'red'
            }else if(board[row][col] == 'yellow'){
                document.getElementsByClassName('col'+ (col+1))[row].style.backgroundColor = 'yellow'
            }
        }
    }
}

function move(event){
    const Http =  new XMLHttpRequest();
    var url = "http://127.0.0.1:5000/move1"
    
    Http.open('POST', url)
    Http.setRequestHeader("Content-Type", "application/json");
    let classNames = event.target.getAttribute('class')
    data = JSON.stringify({'column': classNames.split(' ')[1]})
    Http.responseType = 'text'
    
    Http.send(data)

    Http.onload = function(){
        if(Http.readyState == Http.DONE){
            if(Http.status == 200){
                data = JSON.parse(Http.response)
                if(data['invalid'] == true){
                    console.log(data)
                   //displayBoard(data['move'])
                    if(data['winner'].length > 0){
                        document.getElementById('mstatus').innerHTML =  data['winner'].charAt(0).toUpperCase()+ data['winner'].slice(1) + " Wins!"
                        document.getElementById('status').innerHTML = ""
                        showResetButton()
                    }

                    else{
                        document.getElementById('status').innerHTML = "Error: " + data['reason']
                    }
                    
                }else{
                    displayBoard(data['move'])
                    document.getElementById('status').innerHTML = ""
                    if(data['winner'].length > 0){
                        document.getElementById('mstatus').innerHTML = data['winner'].charAt(0).toUpperCase()+ data['winner'].slice(1) + " Wins!"
                        showResetButton()
                    }
                    else{
                        document.getElementById('mstatus').innerHTML = "Please Wait for Opponent to Make Move"
                    }
                    
                }
                
            }
        }
    }
    
}

function hideLink(){
    document.getElementById("p2Link").style.display = "none"
}
function showResetButton(){
    document.getElementById("resetbtn").removeAttribute("hidden")
}

autoUpdate()