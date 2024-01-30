import {React,useEffect,useState} from "react";
import "./List.css"

function List() {
const[donor,setdonor]=useState([])
useEffect(()=>{
  fetch(`http://127.0.0.1:5000/donor`)
  .then(res=>res.json())
  .then(data=>setdonor(data))
},[])

const handleDeletedata=(id)=>{
  const newData=donor.filter((blog)=> blog.D_id !== id
  )
  setdonor(newData)
}
const handleDelete=(D_id)=>{
  fetch(`http://127.0.0.1:5000/donor/${D_id}`,{
    method:"DELETE"
  })
  handleDeletedata(D_id)
}
  return <div>
    <section className="list">
    <table className="styled-table">
            <thead>
                <tr>
                    <th>D_id</th>
                    <th>Dname</th>
                    <th>Demail</th>
                    <th>sex</th>
                    <th>address</th>
                    <th>age</th>
                    <th>weight</th>
                    <th>donor_Date</th>
                    <th>Action</th>

                </tr>
            </thead>
            <tbody>
                {donor.map((obj)=>(
                    <tr key={obj.D_id}>
                    <td>{obj.D_id}</td>
                    <td>{obj.Dname}</td>
                    <td>{obj.Demail}</td>
                    <td>{obj.sex}</td>
                    <td>{obj.address}</td>
                    <td>{obj.age}</td>
                    <td>{obj.weight}</td>
                    <td>{obj.donor_Date}</td>
                    <td>
                      <button id="button" onClick={()=>handleEdit(obj.D_id)}>Edit</button>
                      <button id="button" onClick={()=>handleDelete(obj.D_id)}>Delete</button>
                    </td>
                     </tr>
                ))}
            </tbody>
        </table>
    </section>   
  </div>;
}

export default List;
