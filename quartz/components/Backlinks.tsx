import { i18n } from "../i18n"
import { classNames } from "../util/lang"
import { resolveRelative, simplifySlug } from "../util/path"
import style from "./styles/backlinks.scss"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

interface BacklinksOptions {
  hideWhenEmpty: boolean
}

const defaultOptions: BacklinksOptions = {
  hideWhenEmpty: true,
}

export default ((opts?: Partial<BacklinksOptions>) => {
  const options: BacklinksOptions = { ...defaultOptions, ...opts }

  const Backlinks: QuartzComponent = ({
    fileData,
    allFiles,
    displayClass,
    cfg,
  }: QuartzComponentProps) => {
    const slug = simplifySlug(fileData.slug!)
    const backlinkFiles = allFiles.filter((file) => file.links?.includes(slug))

    if (slug === "/") {
      return null
    }

    return (
      <div class={classNames(displayClass, "backlinks")}>
        <h3>{i18n(cfg.locale).components.backlinks.title}</h3>
        <ul class="overflow">
          <li>
            <a href="https://www.hwendev.com" class="internal">
              Back to Digital Garden
            </a>
          </li>

          {backlinkFiles.length > 0 &&
            backlinkFiles.map((f) => (
              <li>
                <a href={resolveRelative(fileData.slug!, f.slug!)} class="internal">
                  {f.frontmatter?.title}
                </a>
              </li>
            ))}
        </ul>
      </div>
    )
  }

  Backlinks.css = style

  return Backlinks
}) satisfies QuartzComponentConstructor
