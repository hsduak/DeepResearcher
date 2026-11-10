/* Modified for the DeepResearcher source distribution; see NOTICE. */
/** @type {import('@docusaurus/types').DocusaurusConfig} */
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { createRequire } from 'module';

const require = createRequire(import.meta.url);

export default {
  title: 'GPT Researcher',
  tagline: 'The leading autonomous AI research agent',
  url: 'https://docs.gptr.dev',
  baseUrl: '/',
  onBrokenLinks: 'ignore',
  //deploymentBranch: 'master',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/gptr-logo.png',
  organizationName: 'hsduak',
  trailingSlash: false,
  projectName: 'DeepResearcher',
  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],
  themeConfig: {
    navbar: {
      title: 'GPT Researcher',
      logo: {
        alt: 'GPT Researcher',
        src: 'img/gptr-logo.png',
      },
      items: [
        {
          type: 'doc',
          docId: 'welcome',
          position: 'left',
          label: 'Docs',
        },

        {
          type: 'doc',
          docId: 'faq',
          position: 'left',
          label: 'FAQ',
        },
        {
            href: 'https://github.com/hsduak/DeepResearcher/issues',
            position: 'left',
            label: 'Contact',
        },
        {
          href: 'https://github.com/hsduak/DeepResearcher',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Community',
          items: [
            {
              label: 'Discord',
              href: 'https://github.com/hsduak/DeepResearcher',
            },
            {
              label: 'Twitter',
              href: 'https://github.com/hsduak/DeepResearcher',
            },
            {
              label: 'LinkedIn',
              href: 'https://github.com/hsduak/DeepResearcher',
            },
          ],
        },
        {
          title: 'Company',
          items: [
            {
              label: 'Homepage',
              href: 'https://github.com/hsduak/DeepResearcher',
            },
            {
              label: 'Contact',
              href: 'https://github.com/hsduak/DeepResearcher',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} GPT Researcher.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl:
            'https://github.com/hsduak/DeepResearcher/tree/master/docs',
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  stylesheets: [
    {
        href: "https://cdn.jsdelivr.net/npm/katex@0.13.11/dist/katex.min.css",
        integrity: "sha384-Um5gpz1odJg5Z4HAmzPtgZKdTBHZdw8S29IecapCSB31ligYPhHQZMIlWLYQGVoc",
        crossorigin: "anonymous",
    },
  ],

  plugins: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      {
        hashed: true,
        blogDir:"./blog/"
      },
    ],
  ],
};
