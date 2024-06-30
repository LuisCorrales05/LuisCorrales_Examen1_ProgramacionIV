document.getElementById('register-form').addEventListener('submit', function(event) {
  event.preventDefault();

  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const  number = document.getElementById('number').value;

  fetch('http://localhost:5000/employee/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },

    body: JSON.stringify({name, email, number})
  })
  .then(response => response.json())
  .then(data => {
      if (data.employee_id) {
          alert(`Empleado registrado: ${data.name} (${data.email}) (${data.number})` );
          document.getElementById('name').value = '';
          document.getElementById('email').value = '';
          document.getElementById('number').value = '';  
          addEmployeeToTable(data);
          
      } else {
          alert('Error al registrar empleado');

      }
  })
  .catch(error => console.error('Error:', error));
  console.log(JSON.stringify({ name, email, number }));
});

// Función para agregar un empleado a la tabla
function addEmployeeToTable(employee) {
  const table = document.querySelector('.table-hover tbody');
  const row = document.createElement('tr');
  row.classList.add('table-active');
  row.innerHTML = `
  <td>${employee.employee_id}</td>
  <td>${employee.name}</td>
  <td>${employee.email}</td>
  <td>${employee.number}</td>
  <td>
    <button type="button" class="btn btn-primary" onclick="updateEmployee(${employee.employee_id})">Update</button>
    <button type="button" class="btn btn-danger" onclick="deleteEmployee(${employee.employee_id})">Delete</button>
  </td>
  `;
  table.appendChild(row);
}

// Función para obtener y agregar todos los empleados a la tabla
function getAllEmployees() {
  fetch('http://localhost:5000/employee/employees')
  .then(response => response.json())
  .then(data => {
    data.forEach(employee => {
    addEmployeeToTable(employee);
    });
  })
  .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', (event) => {
  getAllEmployees();
});

// Función para mostrar el modal
function showModal() {
    var modal = document.getElementById('RegistModal');
    modal.style.display = "block";
}

  // Función para cerrar el modal
function closeModal() {
    var modal = document.getElementById('RegistModal');
    modal.style.display = "none";
}

function deleteEmployee(employeeId) {
  fetch(`http://localhost:5000/employee/${employeeId}`, {
      method: 'DELETE'
  })
  .then(response => response.json())
  .then(() => location.reload());
}

function updateEmployee(employeeId) {
  const name = prompt("nuevo name:");
  const email = prompt("nuevo email:");
  const number = prompt("nuevo telefono:");

  fetch(`http://127.0.0.1:5000/employee/${employeeId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, number })
  })
  .then(response => response.json())
  .then(() => location.reload());
  console.log(JSON.stringify({ name, email, number }));

}
