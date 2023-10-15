import React, { useState } from "react";
import axios from "axios";
import { auth } from '../fbase'
import { RecaptchaVerifier, signInWithPhoneNumber } from 'firebase/auth';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Modal from 'react-bootstrap/Modal';
import { useNavigate } from "react-router-dom";



const  Signup = ({ show, setShow }) => {
  const navigate = useNavigate();
  const [name, setName] = useState("");
    const [otp, setOtp] = useState("");
    const [otpBox, openOtpBox] = useState(false);
    const [email,setEmail] = useState("");
    const [phNo, setphNo] = useState("");

    const handleClose = () => setShow(false);

    const submitInfo = () => {
        const usrInfo = {"name":name,"email":email,"phone":phNo}
        axios.post('http://localhost:5000/addUser',usrInfo)
        .then((res)=>{
            console.log(res);
        }).catch((err)=>{
            console.log(err);
        })
    }
    const generateRecapta = () => {
        //window.varName sets up a global variable that can be used anywhere in the app
        ///signin-button is the id of the div where this recapta shall be rendered
        window.recaptchaVerifier = new RecaptchaVerifier(auth, 'sign-in-button', {
            'size': 'invisible',
            'callback': (response) => {
                // reCAPTCHA solved, allow signInWithPhoneNumber.
            }
        });
    }
    const generateOtp = () => {
        openOtpBox(true)
        const phno = "+91" + phNo;
        if (phno.length === 13) {
            generateRecapta();
            let appVerifier = window.recaptchaVerifier;
            signInWithPhoneNumber(auth, phno, appVerifier).then(
                confirmationResult => {
                    window.confirmationResult = confirmationResult;
                }
            ).catch(err => {
                console.log(err);
            })
        } else {
            console.log("Incorrect phone number");
        }

    }
    const verifyOtp = () => {
        if (otp.length === 6) {
            console.log(otp);
            let confirmationResult = window.confirmationResult;
            confirmationResult.confirm(otp).then((result) => {
                // User signed in successfully.
                const user = result.user;
                console.log("Successfully submitted");
                console.log(user);
                // submitInfo();
                navigate('/home')
            }).catch((error) => {
                console.log(error);
            });
        }
    }

    return (
      <>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Sign Up to NewsFeed</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group className="mb-3" controlId="SignupForm.ControlInput1">
            <Form.Label>Name</Form.Label>
            <Form.Control
                type="text"
                autoFocus
                autoComplete="name"
                onChange={(event)=>{setName(event.target.value)}}
              />
            <Form.Label>Phone Number</Form.Label>
            <Form.Control
                type="number"
                autoFocus
                autoComplete="phone"
                onChange={(event)=>{setphNo(event.target.value)}}
              />
              
              <Form.Label>Email address</Form.Label>
              <Form.Control
                type="email"
                placeholder="name@Signup.com"
                autoFocus
                onChange={(event)=>{setEmail(event.target.value)}}
              />
              {otpBox &&<> 
              <Form.Label>OTP</Form.Label>
              <Form.Control
                type="password"
                autoFocus
                onChange={(event)=>{setOtp(event.target.value)}}
              /></>}
            </Form.Group>
            <Form.Group
              className="mb-3"
              controlId="SignupForm.ControlTextarea1"
            >
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          {otpBox ? <Button variant="primary" onClick={verifyOtp}>
            Verify OTP
          </Button>:<Button variant="primary" onClick={generateOtp}>
              Get OTP
          </Button>}
        </Modal.Footer>
      </Modal>
      <div id="sign-in-button"></div>
    </>
    )
}

export default Signup;