export default function Home() {
  return (
    <div className="flex items-center justify-center h-5/6 relative">
      <div className="absolute left-1/2 -translate-x-1/2 -translate-y-1/2">
        <h1 className="font-bold text-[250px] text-white ml-[30px]" style={{ textShadow: '2px 2px 4px rgba(0, 0, 0, 0.3)' }}>SPAZEX</h1>
      </div>
      <div className="absolute left-[650px] mb-10">
        <p className="text-[40px] text-white">Hellenic Outreach and Community Association</p>
      </div>
      <div className="absolute top-[400px] left-[810px] flex space-x-10">
        <button className="text-[24px] text-white rounded-full bg-gradient-to-t from-[#00b1a3] to-[#42cdc2] px-8 py-3 shadow-lg hover:from-red-500 hover:to-red-700 transition ease-in-out duration-300">About</button>
        <button className="text-[24px] text-white rounded-full bg-gradient-to-t from-[#00b1a3] to-[#42cdc2] px-8 py-3 shadow-lg hover:from-red-500 hover:to-red-700 transition ease-in-out duration-300">Sign Up!</button>
      </div>
    </div>
  )
}
