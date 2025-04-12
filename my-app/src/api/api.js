import axios from "axios"


const api = axios.create({
    baseURL:"https://localhost:5000"
})


export async function registerUser(username,password,email){

    const response =await api.post("/register",{
        username,password,email
    })


    return response.data

}

