document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#presentation').addEventListener('click', () => load_content('presentation'));
  document.querySelector('#gouvernance').addEventListener('click', () => load_content('gouvernance'));
  document.querySelector('#references').addEventListener('click', () => load_content('references'));
  document.querySelector('#recrutement').addEventListener('click', () => load_content('recrutement'));
  document.querySelector('#ao').addEventListener('click', () => load_content('ao'));
  document.querySelector('#contact').addEventListener('click', () => load_content('contact'));


  // By default, load the video
  load_content('video');
});

function load_content(content){
    document.querySelector('#presentation-view').style.display = 'none';
    document.querySelector('#gouvernance-view').style.display = 'none';
    document.querySelector('#references-view').style.display = 'none';
    document.querySelector('#recrutement-view').style.display = 'none';
    document.querySelector('#ao-view').style.display = 'none';
    document.querySelector('#contact-view').style.display = 'none';
    document.querySelector('#video-view').style.display = 'none';

    switch (content) {
        case 'presentation':
            document.querySelector('#presentation-view').style.display = 'block';
            break;
        case 'gouvernance':
            document.querySelector('#gouvernance-view').style.display = 'block';
            break;
        case 'references':
            document.querySelector('#references-view').style.display = 'block';
            break;
        case 'recrutement':
            document.querySelector('#recrutement-view').style.display = 'block';
            load_recrutements();
            break;
        case 'ao':
            document.querySelector('#ao-view').style.display = 'block';
            load_aos();
            break;
        case 'contact':
            document.querySelector('#contact-view').style.display = 'block';
            break;
        default:
            document.querySelector('#video-view').style.display = 'block';
    }

}

function load_aos(){
    const table = document.querySelector('#ao-table');
    table.innerHTML = "";
    fetch(`aos`) //getting aos
        .then(response => response.json())
            .then(aos => {
                let th = Object.keys(aos[0]);
                generateTableHead(table, th);
                generateTable(table, aos);
            });
}

function load_recrutements(){
    const table = document.querySelector('#recrutement-table');
    table.innerHTML = "";
    fetch(`recrutements`) //getting recrutements
        .then(response => response.json())
            .then(recrutements => {
                let th = Object.keys(recrutements[0]);
                generateTableHead(table, th);
                generateTable(table, recrutements);
            });

}

//https://www.valentinog.com/blog/html-table/

function generateTableHead(table, data) {
  let thead = table.createTHead();
  let row = thead.insertRow();
  for (let key of data) {
    let th = document.createElement("th");
    th.setAttribute("scope", "col");
    let text = document.createTextNode(key);
    th.appendChild(text);
    row.appendChild(th);
  }
}

function generateTable(table, data) {
  for (let element of data) {
    let row = table.insertRow();
    for (key in element) {
        let cell = row.insertCell();
        var text = document.createTextNode(element[key]);
        if (key==="pdf"){
            text = document.createElement('a');
            text.href = element[key];//window.location.hostname;
            text.innerHTML = 'avis pdf';
        }
        cell.appendChild(text);
    }
  }
}