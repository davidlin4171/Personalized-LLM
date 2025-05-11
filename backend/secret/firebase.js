import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyDes0w650uvrwdhQwCVjHb5gZXJ9PRHsAY",
  authDomain: "personalized-llm-39f52.firebaseapp.com",
  projectId: "personalized-llm-39f52",
  storageBucket: "personalized-llm-39f52.firebasestorage.app",
  messagingSenderId: "542079677127",
  appId: "1:542079677127:web:f57f77201f4119d6a044e2",
  measurementId: "G-QTDNBXPLMX"
};
;

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);