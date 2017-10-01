var node1 = null;
var node2 = null;
var body = null;
var selected = 0;

function navClick(id) {
    selected = id;
    initNavBar();
}


function navClick2() {

    document.getElementById("nav_2").classList.add('active');
    document.getElementById("nav_1").classList.remove('active');

    body.appendChild(node2);
    body.removeChild(node1);

}

function initNavBar() {


    if(selected == 0) {

        //document.getElementById("nav_behandling").classList.add('active');
        //document.getElementById("nav_behandling_text").classList.add('activeText');

    } else if(selected == 1) {


    } else if(selected == 2) {


    } else if(selected == 3) {


    } else if(selected == 4) {


    }

    //document.getElementById("nav_behandling").classList.add('active');
    /*document.getElementById("nav_2").classList.remove('active');

    node1 = document.getElementById("content1");
    node2 = document.getElementById("content2");
    body = document.getElementById("the_body");
    body.removeChild(node2);*/

}

window.onload = function() {

    initNavBar();
};