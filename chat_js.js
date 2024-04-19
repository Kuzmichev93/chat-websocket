let value_enter = document.querySelector('.list_l');
let ip = document.querySelector('.ip');
let list_ip;
let my_ip;
let li;
let get_id;
let fff = document.querySelector('.my_ip');

let button = document.querySelector('.button_message');

let window_message = document.querySelector('.window_message');
let child_window_message;
async function get_my_ip(){
    let url = 'http://192.168.0.104:8060/get_my_ip';

    let respons = await fetch(url,{method: "get",
                       headers:{"Content-Type":"text/html"}
                       })
    my_ip = await respons.text();

}




const socket = new WebSocket("ws://192.168.0.104:1235");
socket.onopen = async ()=>{
    socket.send("browser");

}



async function not_key(mes){
  try{
      document.querySelectorAll(".lis").forEach(el => el.remove());
      }
      catch{}
      await get_my_ip();

      list_ip = mes.data.split(',');


     for(let k=0;k<list_ip.length;k++){
        let value = list_ip[k].replace(/[[', ]/g,'').replace(/]/g,'');
        if(value!=my_ip){
          li = ip.appendChild(document.createElement("li"));
          console.log(value,'jjj')
          li.className = "lis";
          li.id=list_ip[k].replace(/[[', ]/g,'').replace(/]/g,'');
          li.innerText = value}

     }
     await list_ip_all();
     button.addEventListener("click", async (e)=>{ await send_messange(get_id)})

}

socket.onmessage = async (mes)=>{
    try{

       if(/server?/.test(mes.data)){
         console.log(mes.data)
         child_window_message = window_message.appendChild(document.createElement("div"));
         child_window_message.innerText = "От "+mes.data.slice(0,13)+":"+mes.data.slice(20);
         child_window_message.className = "child_window_message";
         //console.log(mes.data)
       }
       else{
       await not_key(mes);
       }
    }
    catch{}
}

async function list_ip_all(){
    //Производится подстветка ip с которым хотим установить соединение.

   const li_all = document.querySelectorAll(".lis");

   for (let k = 0;k<li_all.length;k++){
       li_all[k].addEventListener("click",()=>{
          set_color(get_id,li_all[k])
          li_all[k].style.background = "green";
          get_id = li_all[k].id;
          document.querySelectorAll(".child_window_message").forEach(el => el.remove());


       })
   }
}

async function set_color(get_id,arg){
   //Производится снятие подстветки c ip
   if(get_id){
     if(arg!=get_id){
        document.getElementById(get_id).style.background = "darkgray";
     }
   }
}

async function send_messange(arg){
     let window_bottom = document.querySelector('.window_bottom');
     const msg = arg+"="+window_bottom.value
     child_window_message = window_message.appendChild(document.createElement("div"));
     child_window_message.innerText = "Вы: " + window_bottom.value
     child_window_message.className = "child_window_message";
     await socket.send(msg);
     window_bottom.value='';
}
