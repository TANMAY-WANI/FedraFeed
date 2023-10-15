import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Signup from './Signup';
import { useState } from 'react';
import Login from './Login';

function NavigationBar() {
  const [showSignup,setSignup] = useState(false)
  const [showLogin,setLogin] = useState(false)
  const handleSignUp = ()=>{setSignup(true)}
  const handleLogIn = ()=>{setLogin(true)}
  return (
    <>
      <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand href="#home">FedraFeed</Navbar.Brand>
          <Navbar.Collapse className='justify-content-end'>
          <Nav>
            <Nav.Link href="#home" onClick={handleSignUp}>Sign Up</Nav.Link>
            <Nav.Link href="#features" onClick={handleLogIn}>Log In</Nav.Link>
          </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      {showLogin && <Login show={showLogin} setShow={setLogin}/>}
      {showSignup && <Signup show = {showSignup} setShow = {setSignup}/>}
    </>


  );
}

export default NavigationBar;