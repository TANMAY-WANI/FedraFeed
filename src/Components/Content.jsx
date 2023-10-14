import React, { useState } from 'react'

import Signup from './Signup';

const Content = () => {
    const [signUp,setSignup] = useState(false);
    const handleClick = ()=>{setSignup(true)}
  return (
    <>
    <div className='box'>
        <div>
            <h1 className='heading'>FedraFeed</h1>
            <p className='line1'>Colaborative News Intelligence for All</p>
            <div className='subbox'>
                <p className='line2'>Experience news like never before - tailored just for you</p>
                <button className='btn1' onClick={handleClick}>Get Started</button>
            </div>
        </div>
        <div>
            <img className='image' src="coverimg.png" alt="" />
        </div>
    </div>
    {signUp && <Signup show = {signUp} setShow = {setSignup}/>}
    </>
  )
}

export default Content