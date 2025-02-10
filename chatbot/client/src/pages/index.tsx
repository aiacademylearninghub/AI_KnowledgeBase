import clsx from 'clsx';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';
import Chatbot from "../components/chatbot/chatbot";
import Homepage from "../components/HomePage/Homepage";
import Head from '@docusaurus/Head';
import GlobalHead from '../components/GlobalHead/GlobalHead';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();

  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttonRow} id='container-heading-buttons'>            
        </div>
      </div>
      
    </header>
  );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (  
    <>
    <GlobalHead />  
    <Layout
      title={`Sudeep Aryan ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">  
            
      <HomepageHeader />
      <main>
        <Homepage />        
      </main>
      <Chatbot />
    </Layout>
    </>    
  );
}
