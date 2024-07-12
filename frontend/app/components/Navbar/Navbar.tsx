// components/Navbar/Navbar.tsx
"use client"
import React from 'react'
import Link from 'next/link'
import { useRouter } from 'next/navigation';

const Navbar = () => {
  const router = useRouter()
  return (
    <header className='bg-gradient-to-b from-[#894e34] via-[#9a7e49] to-[#c98455] p-4'>
        <nav className="flex flex-wrap justify-between items-center w-[92%] mx-auto pt-4">
            <div>
                <Link href="/" className='text-white text-xl font-bold'>
                    Spazex
                </Link>
            </div>
            <div className="flex-grow">
                <ul className="flex flex-wrap justify-center items-center gap-4 md:gap-8 lg:gap-8 ml-[120px]">
                <li>
                    <Link href="/about" className="text-white hover:text-gray-500">About</Link>
                </li>
                <li>
                    <Link href="/socratic-circle" className="text-white hover:text-gray-500">Socratic Circle</Link>
                </li>
                <li>
                    <Link href="/mentorships" className="text-white hover:text-gray-500">Mentorships</Link>
                </li>
                <li>
                    <Link href="/outreach" className="text-white hover:text-gray-500">Outreach</Link>
                </li>
                <li>
                    <Link href="/workshops" className="text-white hover:text-gray-500">Workshops</Link>
                </li>
                </ul>
            </div>
            <div className='flex space-x-2'>
                <button 
                className='bg-[#a6c1ee] text-white px-5 py-2 rounded-full hover:bg-[#87acec] mr-2'
                onClick={()=>router.push('/signup')}>Sign up</button>
                <button className='bg-[#a6c1ee] text-white px-5 py-2 rounded-full hover:bg-[#87acec]'>Login</button>
            </div>
        </nav>
    </header>
  )
}

export default Navbar
