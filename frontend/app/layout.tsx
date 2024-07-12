import './globals.css'
import type { Metadata } from 'next'
import { Oswald } from 'next/font/google'
import Navbar from './components/Navbar/Navbar'

const oswald = Oswald({ subsets: ['cyrillic'] });

export const metadata: Metadata = {
  title: 'Spazex',
  description: 'Spazex App',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={oswald.className}>
        <Navbar/>
        {children}
      </body>
    </html>
  )
}
