// Vinext force-exits while Windows native build workers are still closing.
// Let a successful build close its handles naturally; preserve every error exit.
const originalExit=process.exit.bind(process);
process.exit=(code)=>{if(code===0){process.exitCode=0;return;}return originalExit(code);};
