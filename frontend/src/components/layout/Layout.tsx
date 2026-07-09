import { useState } from "react"

import type { Track } from "../../types/track"

import TrackTable from "../library/TrackTable"
import Button from "../ui/Button"
import Panel from "../ui/Panel"

export default function Layout() {
  const [searchQuery, setSearchQuery] = useState("")
  const [selectedTrack, setSelectedTrack] = useState<Track | null>(null)

  return (
    <div className="grid h-screen grid-cols-[260px_1fr_360px] bg-slate-950 text-white">

      {/* Sidebar */}

      <aside className="border-r border-slate-800 bg-slate-950/90 p-6">

        <div className="mb-10 text-2xl font-extrabold tracking-[0.18em]">
          DJOS
        </div>

        <nav className="flex flex-col gap-2">

          <Button active>
            🎵 Library
          </Button>

          <Button>
            📁 Playlists
          </Button>

          <Button>
            🤖 AI Mix
          </Button>

          <Button>
            📊 Analysis
          </Button>

          <Button>
            ⚙ Settings
          </Button>

        </nav>

      </aside>

      {/* Main */}

      <main className="overflow-hidden p-6">

        <header className="mb-5 flex items-center justify-between">

          <div>
            <h1 className="text-3xl font-bold">
              Library
            </h1>

            <p className="text-slate-400">
              Music Intelligence Engine
            </p>
          </div>

          <input
            className="w-80 rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 outline-none transition focus:border-blue-500"
            placeholder="Search tracks..."
            value={searchQuery}
            onChange={(event) =>
              setSearchQuery(event.target.value)
            }
          />

        </header>

        <Panel>

          <TrackTable
            searchQuery={searchQuery}
            onSelectTrack={setSelectedTrack}
          />

        </Panel>

      </main>

      {/* Analysis */}

      <aside className="border-l border-slate-800 bg-slate-950/90 p-6">

        <h2 className="text-2xl font-bold">
          Analysis
        </h2>

        {!selectedTrack && (

          <div className="mt-10 text-slate-400">

            <p>
              Select a track from the library.
            </p>

          </div>

        )}

        {selectedTrack && (

          <div className="mt-6 space-y-5">

            <div>

              <h3 className="text-xl font-semibold">
                {selectedTrack.title}
              </h3>

              <p className="text-slate-400">
                {selectedTrack.artist}
              </p>

            </div>

            <Panel>

              <p className="text-sm text-slate-400">
                BPM
              </p>

              <p className="mt-2 text-4xl font-bold">
                {selectedTrack.bpm ?? "-"}
              </p>

            </Panel>

            <Panel>

              <p className="text-sm text-slate-400">
                Camelot Key
              </p>

              <p className="mt-2 text-4xl font-bold">
                {selectedTrack.camelot_key ?? "-"}
              </p>

            </Panel>

          </div>

        )}

      </aside>

    </div>
  )
}