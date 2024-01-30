import {React,useEffect,useState} from "react";
import "./Donorlist.css"
import { useFormik } from 'formik';
import * as yup from "yup";

function Donorlist() {
  const [customers, setCustomers] = useState([{}]);
  const [refreshPage, setRefreshPage] = useState(false);

  useEffect(() => {
    console.log("FETCH! ");
    fetch("http://127.0.0.1:5000/donor")
      .then((res) => res.json())
      .then((data) => {
        setCustomers(data);
        console.log(data);
      });
  }, [refreshPage]);

  const formSchema = yup.object().shape({
    Demail: yup.string().email("Invalid email").required("Must enter email"),
    Dname: yup.string().required("Must enter a name").max(15),
    age: yup
      .number()
      .positive()
      .integer()
      .required("Must enter age")
      .typeError("Please enter an Integer")
      .max(125),
    sex:yup.string(),
    address:yup.string(),
    weight: yup.string()
  });

  const formik = useFormik({
    initialValues: {
      Dname: '',
      Demail: '',
      sex: '',
      address: '',
      age: '',
      weight: '',
    },
    validationSchema: formSchema,
onSubmit: (values) => {
      fetch("http://127.0.0.1:5000/donor", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values, null, 2),
      }).then(
        (res) => {
          if (res.status == 200){
            setRefreshPage(!refreshPage)
          }
        }
      )
    },
  });
  return <div>
    <section className="home">
     <main>
        <form onSubmit={formik.handleSubmit}>
          <div>
            <label for="name">DonorName</label>
            <input 
            id="name"
            type="text" 
            name="Dname"
            onChange={formik.handleChange}
            value={formik.values.firstName}
            />
          </div>
          <div>
            <label for="email">Donor Email</label>
            <input 
            id="email" 
            type="email" 
            name="Demail"
            onChange={formik.handleChange}
            value={formik.values.firstName}
            />
          </div>
          <div>
            <label for="sex">Sex</label>
            <input 
            id="sex" 
            type="text" 
            name="sex"
            onChange={formik.handleChange}
            value={formik.values.firstName}
            />
          </div>
          <div>
            <label for="address">Address</label>
            <input 
            id="address" 
            type="address"
            name="address"
            onChange={formik.handleChange}
            value={formik.values.firstName}
             />
          </div>
          <div>
            <label for="Age">Age</label>
            <input 
            id="Age" 
            type="number" 
            name="age"
            onChange={formik.handleChange}
            value={formik.values.firstName}
            />
          </div>    
          <div>
            <label for="Weight">Weight</label>
            <input 
            id="Weight"
            type="number"
            name="weight"
            onChange={formik.handleChange}
            value={formik.values.firstName}
            />
          </div>             
          {/* <div>
            <label for="comp">Favorite CSS Compiler</label>
            <select id="comp">
              <option value="sass">Sass</option>
              <option value="less">Less</option>
              <option value="stylus">Stylus</option>
              <option value="postcss">PostCSS</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div>
            <fieldset>
              <legend>Are you familiar with CSS Grid?</legend>
              <input type="radio" name="grid" id="yes" value="yes" />
              <label for="yes">Yes</label>
              <input type="radio" name="grid" id="no" value="no" />
              <label for="no">No</label>
            </fieldset>
          </div>
          <div class="full-width">
            <label for="message">Message</label>
            <textarea id="message"></textarea>
          </div>
          <div class="full-width">
            <input type="checkbox" id="newsletter" />
            <label for="newsletter">Receive our newsletter?</label>
          </div> */}
          <div class="full-width">
            <button type="submit">Submit</button>
            <button type="reset">Clear Form</button>
          </div>
        </form>
      </main>
    </section>
  </div>;
}

export default Donorlist;
