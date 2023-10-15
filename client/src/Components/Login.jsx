import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Modal from 'react-bootstrap/Modal';
import { useState } from 'react';
import axios from 'axios';
function Login({show,setShow}) {

    //state variables
    const [otpBox, openOtpBox] = useState(false);
    const [otp, setOtp] = useState("");
    const [phNo, setphNo] = useState("");

    const checkIfNotRegistered = () => {
        const data = {
            "phone": phNo
        }
        axios.post('http://localhost:5000/checkUser', data)
        .then((res) => {
            console.log(res);
            if (res.data) {
                generateOtp();
            } else {
                alert("You are not registered. Please register first");
            }
        }).catch((err) => {
            console.log(err);
        }
        )
    }
    //functions
    const generateRecapta = () => {
        //window.varName sets up a global variable that can be used anywhere in the app
        ///signin-button is the id of the div where this recapta shall be rendered
        window.recaptchaVerifier = new RecaptchaVerifier('signin-button', {
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
      };
    const verifyOtp = () => {
        if (otp.length === 6) {
            console.log(otp);
            let confirmationResult = window.confirmationResult;
            confirmationResult.confirm(otp).then((result) => {
                console.log(result);
            }).catch((err) => {
                console.log(err);
            })
        }
    }



  const handleClose = () => setShow(false);
  return (
    <>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Log In</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group className="mb-3" controlId="SignupForm.ControlInput1">
            <Form.Label>Phone Number</Form.Label>
            <Form.Control
                autoComplete='phone'
                type="number"
                autoFocus
              />
              <Form.Label>OTP</Form.Label>
            <Form.Control
                type="number"
                autoFocus
              />
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
          </Button>:<Button variant="primary" onClick={checkIfNotRegistered}>
              Get OTP
          </Button>}
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default Login;