import type { Track } from "../../types/track"
import { useTracks } from "../../hooks/useTracks"

type Props = {
  searchQuery: string
  onSelectTrack: (track: Track) => void
}

export default function TrackTable({ searchQuery, onSelectTrack }: Props) {
  const { tracks, loading } = useTracks()

  const filteredTracks = tracks.filter((track) => {
    const query = searchQuery.toLowerCase()

    return (
      track.artist.toLowerCase().includes(query) ||
      track.title.toLowerCase().includes(query)
    )
  })

  if (loading) {
    return <p className="text-slate-400">Loading tracks...</p>
  }

  return (
    <table className="w-full border-collapse text-sm">
      <thead className="sticky top-0 bg-slate-900">
        <tr className="border-b border-slate-800 text-left text-xs uppercase tracking-wider text-slate-400">
          <th className="px-4 py-3">Artist</th>
          <th className="px-4 py-3">Title</th>
          <th className="px-4 py-3 text-center">BPM</th>
          <th className="px-4 py-3 text-center">Key</th>
        </tr>
      </thead>

      <tbody>
        {filteredTracks.map((track) => (
          <tr
            key={track.id}
            onClick={() => onSelectTrack(track)}
            className="cursor-pointer border-b border-slate-800 text-slate-200 hover:bg-blue-500/10"
          >
            <td className="px-4 py-3">{track.artist}</td>
            <td className="px-4 py-3">{track.title}</td>
            <td className="px-4 py-3 text-center">{track.bpm ?? "-"}</td>
            <td className="px-4 py-3 text-center">{track.camelot_key ?? "-"}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}