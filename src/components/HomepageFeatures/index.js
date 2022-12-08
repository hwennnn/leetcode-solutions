import clsx from 'clsx';
import React from 'react';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Easy to Read',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        The solutions on the site will be presented in a clear and
        easy-to-understand format, making it accessible to a wide range
        of users, regardless of their prior coding experience.
      </>
    ),
  },
  {
    title: 'Always in Sync',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        The site will be regularly updated with new solutions and problems,
        ensuring that users have access to the latest and most relevant content.
        This will help them stay on top of the rapidly changing landscape of
        coding challenges and prepare for the latest trends in the industry.
      </>
    ),
  },
  {
    title: 'Comprehensive Collection',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        The site will provide a comprehensive collection of solutions to Leetcode problems,
        making it a valuable resource for anyone looking to improve their coding skills
        and prepare for technical interviews.
      </>
    ),
  },
];

function Feature({ Svg, title, description }) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
