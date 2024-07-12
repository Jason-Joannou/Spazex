"use client";
import React, { useState } from 'react';
import axios from 'axios';

const SignupPage = () => {
  const [formData, setFormData] = useState({
    spaza_email: '',
    spaza_name: '',
    spaza_password: '',
    spaza_reg_no: '',
  });

  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:8080/register_spaza', formData);
      setSuccess('User created successfully!');
      setError('');
    } catch (error) {
      setError(`There was an error creating the user. ${error}`);
      setSuccess('');
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen pb-32">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        <h2 className="text-2xl font-bold mb-6">Sign Up</h2>
        {error && <p className="text-red-500">{error}</p>}
        {success && <p className="text-green-500">{success}</p>}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="spaza_email" className="block text-gray-700">Email:</label>
            <input
              type="email"
              id="spaza_email"
              name="spaza_email"
              className="w-full p-2 border border-gray-300 rounded mt-1"
              value={formData.spaza_email}
              onChange={handleChange}
            />
          </div>
          <div className="mb-4">
            <label htmlFor="spaza_name" className="block text-gray-700">Spaza Name:</label>
            <input
              type="text"
              id="spaza_name"
              name="spaza_name"
              className="w-full p-2 border border-gray-300 rounded mt-1"
              value={formData.spaza_name}
              onChange={handleChange}
            />
          </div>
          <div className="mb-4">
            <label htmlFor="spaza_password" className="block text-gray-700">Password:</label>
            <input
              type="password"
              id="spaza_password"
              name="spaza_password"
              className="w-full p-2 border border-gray-300 rounded mt-1"
              value={formData.spaza_password}
              onChange={handleChange}
            />
          </div>
          <div className="mb-4">
            <label htmlFor="spaza_reg_no" className="block text-gray-700">Spaza Shop Registration Number:</label>
            <input
              type="text"
              id="spaza_reg_no"
              name="spaza_reg_no"
              className="w-full p-2 border border-gray-300 rounded mt-1"
              value={formData.spaza_reg_no}
              onChange={handleChange}
            />
          </div>
          <button
            type="submit"
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 w-full"
          >
            Sign Up
          </button>
        </form>
      </div>
    </div>
  );
};

export default SignupPage;