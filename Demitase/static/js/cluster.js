function show_add_cluster() {
    document.getElementById("add_cluster").style.display = "block";
}
function add_cluster() {
    var form = document.getElementById("add_cluster").children[0];
    var csrf_token = form.getElementsByTagName("input")[0].getAttribute("value");
    var new_cluster = form.elements["name"].value;
    var body = "name="+new_cluster;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/add-cluster/", false);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.setRequestHeader("X-CSRFToken", csrf_token);
    xmlhttp.send(body);
    document.location.reload(true);
}
function delete_cluster(cluster) { //DELETE CLUSTER TAB(CONTAINER)
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/delete-cluster/"+cluster+"/", false);
    xmlhttp.send();
    galera_init(); 
    document.location.reload(true);
    
}

function setup_galera_cluster(cluster) { //
    var xmlhttp = new XMLHttpRequest();
    //xmlhttp.open("GET", "/delete-cluster/"+cluster+"/galera-remove/", false);
    xmlhttp.open("GET", "/setup-galera-cluster/"+cluster+"/", false);
    xmlhttp.send();
    document.location.reload(true);
}

function setup_rabbitmq_cluster(cluster) { //
    var xmlhttp = new XMLHttpRequest();
    //xmlhttp.open("GET", "/delete-cluster/"+cluster+"/galera-remove/", false);
    xmlhttp.open("GET", "/setup-rabbitmq-cluster/"+cluster+"/", false);
    xmlhttp.send();
    document.location.reload(true);
}

function remove_galera_cluster(cluster) { //
    var xmlhttp = new XMLHttpRequest();
    //xmlhttp.open("GET", "/delete-cluster/"+cluster+"/galera-remove/", false);
    xmlhttp.open("GET", "/remove-galera-cluster/"+cluster+"/", false);
    xmlhttp.send();
    document.location.reload(true);
}

function remove_rabbitmq_cluster(cluster) { //
    var xmlhttp = new XMLHttpRequest();
    //xmlhttp.open("GET", "/delete-cluster/"+cluster+"/galera-remove/", false);
    xmlhttp.open("GET", "/remove-rabbitmq-cluster/"+cluster+"/", false);
    xmlhttp.send();
    document.location.reload(true);
}

function staus_galera_cluster(cluster) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/status-galera-cluster/"+cluster+"/", false);
    xmlhttp.send();
}
function staus_rabbitmq_cluster(cluster) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/status-rabbitmq-cluster/"+cluster+"/", false);
    xmlhttp.send();
}

function update_server() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/servers/", false);
    xmlhttp.send();
    document.getElementById("servers").innerHTML = xmlhttp.responseText;
    eval(document.getElementById("servers").getElementsByTagName("script")[0].innerText);
}


function update_galera() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/galera-nodes/", false);
    xmlhttp.send();
    //document.getElementById("servers").innerHTML = xmlhttp.responseText;
    //eval(document.getElementById("servers").getElementsByTagName("script")[0].innerText);
    galera_init()
}
function update_network() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/network-topology/", false);
    xmlhttp.send();
    //document.getElementById("servers").innerHTML = xmlhttp.responseText;
    //eval(document.getElementById("servers").getElementsByTagName("script")[0].innerText);
    network_init()
}
function update_rabbitmq() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/rabbitmq-nodes/", false);
    xmlhttp.send();
    //document.getElementById("servers").innerHTML = xmlhttp.responseText;
    //eval(document.getElementById("servers").getElementsByTagName("script")[0].innerText);
    rabbitmq_init()
}

function update_galera_node() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/galera-nodes/", false);
    xmlhttp.send();
    document.getElementById("galera-nodes").innerHTML = xmlhttp.responseText;
    eval(document.getElementById("galera-nodes").getElementsByTagName("script")[0].innerText);
}
function update_network_topology() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/network/", false);
    xmlhttp.send();
    document.getElementById("network-topology").innerHTML = "<iframe src='http://61.43.139.95:8000/network/' width='100%' height='780px' scrolling='yes'></iframe>";
   // document.getElementById("network-topology").innerHTML = xmlhttp.responseText;
   //eval(document.getElementById("network-topology").getElementsByTagName("script")[0].innerText);
}

function update_rabbitmq_node() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/rabbitmq-nodes/", false);
    xmlhttp.send();
    document.getElementById("rabbitmq-nodes").innerHTML = xmlhttp.responseText;
    eval(document.getElementById("rabbitmq-nodes").getElementsByTagName("script")[0].innerText);
}


function update_add_server() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/add-server/", false);
    xmlhttp.send();
    document.getElementById("add-server").innerHTML = xmlhttp.responseText;
}

function update_add_galera_node() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/add-galera-node/", false);
    xmlhttp.send();
    document.getElementById("add-galera-node").innerHTML = xmlhttp.responseText;
}

function start_galera_node(server_name) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/start-galera-node/" + server_name + "/", false);
    xmlhttp.send();
    //document.getElementById("start-galera-node").innerHTML = xmlhttp.responseText;
}

function stop_galera_node(server_name) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/stop-galera-node/"+ server_name +"/", false);
    xmlhttp.send();
    //document.getElementById("start-galera-node").innerHTML = xmlhttp.responseText;
}

function update_add_rabbitmq_node() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/add-rabbitmq-node/", false);
    xmlhttp.send();
    document.getElementById("add-rabbitmq-node").innerHTML = xmlhttp.responseText;
}

function start_rabbitmq_node(server_name) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/start-rabbitmq-node/" + server_name + "/", false);
    xmlhttp.send();
    //document.getElementById("start-galera-node").innerHTML = xmlhttp.responseText;
}

function stop_rabbitmq_node(server_name) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/stop-rabbitmq-node/"+ server_name +"/", false);
    xmlhttp.send();
    //document.getElementById("start-galera-node").innerHTML = xmlhttp.responseText;
}

function update_hdfs(cmd, path) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/hdfs/"+curr_cluster+"/"+cmd+path, false);
    xmlhttp.send();
    document.getElementById("hdfs").innerHTML = xmlhttp.responseText;
}
function update_mapreduce() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/mapreduce/"+curr_cluster+"/launch/", false);
    xmlhttp.send();
    document.getElementById("mapreduce").innerHTML = xmlhttp.responseText;
}
function show_add_server() {
    document.getElementById("add-server").style.display = "block";
}
function hide_add_server() {
    document.getElementById("add-server").style.display = "none";
}
function add_server() {
    var form = document.getElementById("add-server").children[0];
    var csrf_token = form.getElementsByTagName("input")[0].getAttribute("value");
    var name = form.elements["name"].value;
    form.elements["name"].value = "";
    var image = form.elements["image"].value;
    var flavor = form.elements["flavor"].value;
    var body = "name="+name+"&image="+image+"&flavor="+flavor;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/cluster/"+curr_cluster+"/add-server/", false);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.setRequestHeader("X-CSRFToken", csrf_token);
    xmlhttp.send(body);
    update_server();
}
/*
function add_galera_server() {
    var form = document.getElementById("add-server").children[0];
    var csrf_token = form.getElementsByTagName("input")[0].getAttribute("value");
    var name = form.elements["name"].value;
    form.elements["name"].value = "";
    var image = form.elements["image"].value;
    var flavor = form.elements["flavor"].value;
    var body = "name="+name+"&image="+image+"&flavor="+flavor;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/cluster/"+curr_cluster+"/add-server/", false);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.setRequestHeader("X-CSRFToken", csrf_token);
    xmlhttp.send(body);
    update_server();
}
*/
function delete_server(server_name, server_id) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/delete-server/"+server_name+"/"+server_id+"/", false);
    xmlhttp.send();
    update_server();
}


function delete_galera_node(server_name, server_id) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/delete-galera-node/"+server_name+"/"+server_id+"/", false);
    xmlhttp.send();
    update_galera_node();
    update_add_galera_node();
    document.location.reload(true);

}

function initdb_galera_node(server_name) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/initdb-galera-node/"+server_name+"/", false);
    xmlhttp.send();
    //update_galera_node();
    //update_add_galera_node();
    //document.location.reload(true);
}

function sync_galera_node(server_name) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/sync-galera-node/"+server_name+"/", false);
    xmlhttp.send();
    //update_galera_node();
    //update_add_galera_node();
    //document.location.reload(true);
}

function delete_rabbitmq_node(server_name, server_id) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/delete-rabbitmq-node/"+server_name+"/"+server_id+"/", false);
    xmlhttp.send();
    update_rabbitmq_node();
    update_add_rabbitmq_node();
}

function install_role(server_name, role) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/server/"+server_name+"/install/"+role+"/", false);
    xmlhttp.send();
    update_server();
}

function install_role_bm(server_name, role) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/galera-node/"+server_name+"/install/"+role+"/", false);
    xmlhttp.send();
    //update_server();
    update_galera_node();
}

/*
function install_role(server_name, role) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/server/"+server_name+"/install/"+role+"/", false);
    xmlhttp.send();
    update_server();
}
*/

function uninstall_role(server_name, role) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/cluster/"+curr_cluster+"/server/"+server_name+"/uninstall/"+role+"/", false);
    xmlhttp.send();
    update_server();
}
function init() {
    update_server();
    update_add_server();
    if (has_master) {
        update_hdfs('show','/');
        update_mapreduce();
    }
}

function galera_init() {
    update_galera_node();
    update_add_galera_node();
}


function rabbitmq_init() {
    update_rabbitmq_node();
    update_add_rabbitmq_node();
}

function network_init() {
    update_network_topology();
    //update_add_galera_node();
}
