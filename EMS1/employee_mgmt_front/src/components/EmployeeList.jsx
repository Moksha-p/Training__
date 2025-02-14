import React, { useEffect, useState } from "react";
import axios from "axios";

const EmployeeList = () => {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/employees/employees/")
      .then((response) => {
        setEmployees(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.log("Error fetching employees", error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading employees...</div>;
  }
  console.log(employees)
  return (
    <div>
      <h1>Employee List</h1>
      {employees.length > 0 ? (
        <ul>
          {employees.map((employee) => (
            <li key={employee.id}>{employee.name}</li>
          ))}
        </ul>
      ) : (
        <p>No employees found.</p>
      )}
    </div>
  );
};

export default EmployeeList;
