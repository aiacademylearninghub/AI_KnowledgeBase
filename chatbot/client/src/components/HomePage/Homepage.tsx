import React, { useState } from 'react';
import { Tabs, Tab, Box } from '@mui/material';
import GraphComponent from '../Graph/NewGraph';
import DecisionTree from '../decisionTree/DecisionTree';
import './Homepage.css';

const Homepage = () => {
  const [selectedTab, setSelectedTab] = useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setSelectedTab(newValue);
  };

  return (
    <Box sx={{ width: '100%' }}>
      <Tabs value={selectedTab} onChange={handleChange} aria-label="basic tabs example">
        <Tab className='knowledgeGraph'  label={<span className="customTabLabel">Knowledge Graph</span>} />
        <Tab className='buildArchitecture' label={<span className="customTabLabel">Build Architecture</span>} />
      </Tabs>
      <Box>
        {selectedTab === 0 && <GraphComponent />}
        {selectedTab === 1 && <DecisionTree />}
      </Box>
    </Box>
  );
};

export default Homepage;