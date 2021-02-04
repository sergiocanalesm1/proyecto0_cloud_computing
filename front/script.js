const url = "http://127.0.0.1:5000/";
const registerEndpoint = "auth";
const loginEndpoint = "user";
const eventListEndpoint = "user_events/";
const createEventsEndpoint = "events";
const eventEndpoint = "event";

const post = "POST";
const put = "PUT";

document.getElementById( "btn-registry" ).onclick = register;
document.getElementById( "btn-login" ).onclick = login;
document.getElementById( "input-username" ).onkeyup = checkEmpty;
document.getElementById( "input-password" ).onkeyup = checkEmpty;

function checkEmpty() {
    if( document.getElementById( "input-username" ).value === "" || document.getElementById( "input-password" ).value === "" ) {
        document.getElementById( "btn-login" ).disabled = true;
        document.getElementById( "btn-registry" ).disabled = true;
    }
    else {
        document.getElementById( "btn-login" ).disabled = false;
        document.getElementById( "btn-registry" ).disabled = false;
    }
}

function register() { 
    auth( registerEndpoint );
 }

 function login() {
     auth( loginEndpoint );
 }


function auth( endpoint ) {
    let json = {
        username : document.getElementById( "input-username" ).value,
        password : document.getElementById( "input-password" ).value
    };
    fetch(
        `${ url }${ endpoint }`,
        {
            method : "POST",
            headers : {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify( json )
        }
    )
    .then( response => response.json() )
    .then( data => initPage( data[ "id" ] ) )
    .catch( (error) =>  console.error( 'Error:', error ) );
}

function initPage( userId ) {
    localStorage.setItem( "userId", parseInt( userId ) )
    document.getElementById( "login" ).hidden = true;
    document.getElementById( "home" ).hidden = false;
    getEvents();
}

document.getElementById( "btn-list" ).onclick = getEvents;

function getEvents() {
    document.getElementById( "div-fill" ).hidden = true;
    let userId = localStorage.getItem( "userId" );
    //userId = 1;
    fetch(
        `${ url }${ eventListEndpoint }${ userId }`,
    )
    .then( response => response.json() )
    .then( data => listEvents( data ) )
}

function listEvents( events ) {
    let html = '<div id="accordion">';
    for( let i = 0; i < events.length; i++ ) {
        html +=
        `
        <div class="card">
            <div class="card-header" id="heading${ i }">
                <h5 class="mb-0">
                    <button class="btn btn-link" data-toggle="collapse" data-target="#collapse${ i }" aria-expanded="false" aria-controls="collapse${ i }">
                        ${ events[ i ].name }
                    </button>
                </h5>
            </div>
            <div id="collapse${ i }" class="collapse" aria-labelledby="heading${ i }" data-parent="#accordion">
                <div class="card-body">
                    <ul>
                        <li> Nombre : ${ events[ i ].name } </li>
                        <li> Categoría : ${ events[ i ].category } </li>
                        <li> Lugar : ${ events[ i ].place } </li>
                        <li> Dirección : ${ events[ i ].address } </li>
                        <li> Fecha de Inicio : ${ events[ i ].start_date } </li>
                        <li> Fecha de Finalización : ${ events[ i ].end_date } </li>
                        <li> Virtual : ${ isVirtual( events[ i ].is_virtual ) } </li>
                    </ul>
                    <br>
                    <div class="d-flex justify-content-center">
                        <input type="button" id="btn-edit" value="Editar" onclick="setupEditEvent( ${ events[ i ].id } )">
                        <input type="button" id="btn-delete" value="Eliminar" onclick="eliminarEvento( ${ events[ i ].id } )">
                    </div>
                </div>
            </div>
        </div>
        `
    }
    html += '</div>'
    document.getElementById( "div-list" ).innerHTML = html;
}

function isVirtual( bool ) {
    return bool ? "Sí" : "No";
}

document.getElementById( "btn-create" ).onclick = setupCreateEvent;

function setupCreateEvent() {
    let acc = document.getElementById( "accordion" );
    if( acc != null ) {
        acc.hidden = true;
    }
    document.getElementById( "div-fill" ).hidden = false;
    document.getElementById( "div-list" ).innerHTML = "<p class='details'>Llene el siguiente formulario completamente.\nSi deja algún campo vacío, no se registrará su evento</p>"
    localStorage.setItem( "endpoint", createEventsEndpoint );
    localStorage.setItem( "method", post );

}

document.getElementById( "btn-send" ).onclick = function() {
    let endpoint = localStorage.getItem( "endpoint" );
    let method = localStorage.getItem( "method" );
    let json = createEventJson();
    fetch(
        `${ url }${ endpoint }`,
        {
            method : method,
            headers : {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify( json )
        }
    )
    .then( response => response.json() )
    .then( data => {
            console.log( data );
            document.getElementById( "div-list" ).innerHTML = "";
            document.getElementById( "div-fill" ).hidden = true;
        }
    )
    .catch( (error) =>  console.error( 'Error:', error ) );
}

function createEventJson() {
    let userId = localStorage.getItem( "userId" );
    let category = document.getElementById( "input-category" ).value;
    let name = document.getElementById( "input-name" ).value
    let place = document.getElementById( "input-place" ).value;
    let address = document.getElementById( "input-address" ).value;
    let start_date = document.getElementById( "input-start-date" ).value;
    let end_date = document.getElementById( "input-end-date" ).value;
    let is_virtual = document.getElementById( "input-is-virtual" ).value;
    
    json = {};
    if( category != null && category  != "" ) {
        json[ "category" ] = category;
    }
    if( name != null && name != "" ) {
        json[ "name" ] = name;
    }
    if( place != null && place != "" ) {
        json[ "place" ] = place;
    }
    if( address != null && address != "" ) {
        json[ "address" ] = address;
    }
    if( start_date != null && start_date != "" ) {
        json[ "start_date" ] = start_date;
    }
    if( end_date != null && end_date != "" ) {
        json[ "end_date" ] = end_date;
    }
    if( is_virtual != null && is_virtual != "" ) {
        json[ "is_virtual" ] = is_virtual == "virtual" ? true : false;
    }
    json[ "user_id" ] = userId;

    return json;

}

function setupEditEvent( id ) {
    let acc = document.getElementById( "accordion" );
    if( acc != null ) {
        acc.hidden = true;
    }
    document.getElementById( "div-fill" ).hidden = false;
    document.getElementById( "div-list" ).innerHTML = "<p class='details'>Llene el siguiente formulario con lo que desee editar.\nSi deja algún el campo vacío, se mantendrá como estaba anteriormente</p>"
    localStorage.setItem( "endpoint", `${ eventEndpoint }/${ id }`  );
    localStorage.setItem( "method", put );
}

function eliminarEvento( id ) {
    fetch(
        `${ url }${ eventEndpoint }/${ id }`,
        {
            method : "DELETE",
        }
    )
    .then( data => {
        document.getElementById( "div-list" ).innerHTML = "";
    } )
    .catch( (error) =>  console.error( 'Error:', error ) );
}
