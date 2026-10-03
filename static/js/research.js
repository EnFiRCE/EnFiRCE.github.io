"use strict";
// Display only the summary copied from a completed, checksum-verified run.
async function loadResults() {
  const status = document.getElementById("data-status");
  try {
    const response = await fetch("static/results/website_summary.json");
    if (!response.ok) throw new Error("Result summary unavailable");
    const data = await response.json();
    if (data.state !== "complete") throw new Error("Result release is incomplete");
    for (const [id, value] of Object.entries({
      "factor-count": data.factorRuns, "baseline-count": data.baselineRuns,
      "packet-count": data.pairedPackets, "check-count": data.engineeringChecks
    })) document.getElementById(id).textContent = String(value);
    const sceneNames = {three_contact: "Three contacts", spatial_sliding: "Spatial sliding"};
    const methodNames = {full: "EnFiRCE", point: "Adapted point LS", gaussian: "Adapted Gaussian LS"};
    const body = document.getElementById("comparison-rows");
    for (const row of data.nominalGroups) {
      const tr = document.createElement("tr");
      if (row.method === "full") tr.className = "enfirce";
      for (const value of [sceneNames[row.scene], methodNames[row.method],
        row.contactRmseN?.mean.toFixed(3) ?? "unmatched",
        row.tipRmseN?.mean.toFixed(3) ?? "unavailable",
        row.totalRmseN?.mean.toFixed(3) ?? "unavailable", row.reviewFrames, row.nonpositiveExits]) {
        const cell = document.createElement("td");
        cell.textContent = String(value);
        tr.appendChild(cell);
      }
      body.appendChild(tr);
    }
    document.getElementById("comparison-conclusion").textContent = data.comparisonConclusion;
    document.getElementById("release-date").textContent = "Results updated " + data.releaseDate + ".";
    status.textContent = data.pairedPackets + " archived packets × 3 methods; 3 noise draws per noisy condition, with identical clean controls. "
      + "Factor/baseline exceptions: " + data.factorExceptions + "/" + data.baselineExceptions
      + ". Nonpositive final exits: " + data.factorNonpositiveExits + "/" + data.baselineNonpositiveExits + ".";
  } catch (error) {
    status.textContent = "The result summary could not be loaded. Download the raw data and provenance from Resources.";
    status.classList.add("error");
    console.error(error);
  }
}
loadResults();
