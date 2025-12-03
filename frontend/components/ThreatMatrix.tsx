import React from 'react';

interface ThreatProps {
  phase: string;
  mitreCode: string;
  technique: string;
}

const ThreatMatrix: React.FC<{ threats: ThreatProps[] }> = ({ threats }) => {
  
  const killChainStages = [
    "Reconnaissance", "Weaponization", "Delivery", 
    "Exploitation", "Installation", "C2", "Actions on Objectives"
  ];

  return (
    <div className="p-6 bg-slate-900 text-white">
      <h2 className="text-xl font-bold mb-4">Live Kill Chain Correlation</h2>
      
      <div className="flex justify-between gap-2">
        {killChainStages.map((stage) => {
          // Find if we have an active threat in this stage
          const activeThreat = threats.find(t => t.phase === stage);
          
          return (
            <div 
              key={stage}
              className={`flex-1 border p-4 rounded ${
                activeThreat ? 'border-red-500 bg-red-900/20' : 'border-slate-700'
              }`}
            >
              <h3 className="text-sm font-semibold text-slate-400 uppercase">{stage}</h3>
              
              {activeThreat && (
                <div className="mt-2 animate-pulse">
                  <div className="text-red-400 font-mono text-xs">
                    {activeThreat.mitreCode}
                  </div>
                  <div className="text-white text-sm font-bold">
                    {activeThreat.technique}
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default ThreatMatrix;
