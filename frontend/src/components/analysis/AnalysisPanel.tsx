import type { Track } from "../../types/track"
import { useTrackAnalysis } from "../../hooks/useTrackAnalysis"

import Panel from "../ui/Panel"

type Props = {
  selectedTrack: Track | null
}

export default function AnalysisPanel({ selectedTrack }: Props) {
  const { analysis, loading } = useTrackAnalysis(
    selectedTrack?.id ?? null,
  )

  if (!selectedTrack) {
    return (
      <aside className="border-l border-slate-800 bg-slate-950/90 p-6">
        <h2 className="text-2xl font-bold">Analysis</h2>

        <p className="mt-10 text-slate-400">
          Select a track from the library.
        </p>
      </aside>
    )
  }

  return (
    <aside className="overflow-y-auto border-l border-slate-800 bg-slate-950/90 p-6">
      <h2 className="text-2xl font-bold">Analysis</h2>

      <div className="mt-6 space-y-5">
        <div>
          <h3 className="text-xl font-semibold">
            {selectedTrack.title}
          </h3>

          <p className="text-slate-400">
            {selectedTrack.artist}
          </p>
        </div>

        {loading && (
          <p className="text-slate-400">
            Loading analysis...
          </p>
        )}

        {analysis && (
          <>
            <div className="grid grid-cols-2 gap-3">
              <Panel>
                <p className="text-sm text-slate-400">BPM</p>
                <p className="mt-2 text-3xl font-bold">
                  {analysis.analysis.bpm ?? "-"}
                </p>
              </Panel>

              <Panel>
                <p className="text-sm text-slate-400">Key</p>
                <p className="mt-2 text-3xl font-bold">
                  {analysis.analysis.camelot_key ?? "-"}
                </p>
              </Panel>
            </div>

            <Panel>
              <p className="mb-3 text-sm text-slate-400">
                Rhythm Intelligence
              </p>

              <div className="grid grid-cols-3 gap-3 text-center">
                <div>
                  <p className="text-2xl font-bold">
                    {analysis.beats.length}
                  </p>
                  <p className="text-xs text-slate-400">Beats</p>
                </div>

                <div>
                  <p className="text-2xl font-bold">
                    {analysis.bars.length}
                  </p>
                  <p className="text-xs text-slate-400">Bars</p>
                </div>

                <div>
                  <p className="text-2xl font-bold">
                    {analysis.phrases.length}
                  </p>
                  <p className="text-xs text-slate-400">Phrases</p>
                </div>
              </div>
            </Panel>

            <Panel>
              <p className="mb-3 text-sm text-slate-400">
                Structure Candidates
              </p>

              <p className="text-3xl font-bold">
                {analysis.change_points.length}
              </p>

              <p className="text-xs text-slate-400">
                Change points detected
              </p>
            </Panel>
          </>
        )}
      </div>
    </aside>
  )
}