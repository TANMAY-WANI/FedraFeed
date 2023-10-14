// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyC04TqKtzsrXK3iQyFug4O205cVs6_nKiQ",
  authDomain: "fedrafeed.firebaseapp.com",
  projectId: "fedrafeed",
  storageBucket: "fedrafeed.appspot.com",
  messagingSenderId: "997131083944",
  appId: "1:997131083944:web:10d34a95b46d26c174a29d",
  measurementId: "G-WYH66EW1P2"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);