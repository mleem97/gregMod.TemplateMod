# Greg Framework ecosystem naming convention

This document defines the authoritative naming and classification rules for the Greg Framework ecosystem.

## 1. Scope

The **Greg Framework** is the umbrella ecosystem for:

- all repositories whose name starts with or prominently contains `greg` or `Greg`;
- all projects, mods, plugins, libraries, tools, websites, documentation and infrastructure built specifically for the game **Data Center**;
- all compatibility, interop, asset, mod-distribution and developer tooling whose primary purpose is to support Data Center or the Greg Framework.

A Data Center repository without a `greg` prefix is considered a legacy naming exception and must be renamed, consolidated or explicitly documented as an upstream fork.

Unrelated Meyer Media products must not receive the `greg` prefix merely because they reuse common CI, MMUI or infrastructure.

## 2. Canonical repository prefixes

| Prefix | Repository type | Examples |
| --- | --- | --- |
| `gregMod.<Name>` | Data Center gameplay, UI or feature mod deployed to `Mods/` | `gregMod.IPAM`, `gregMod.Inventory` |
| `gregPlugin.<Name>` | early MelonLoader plugin deployed to `Plugins/` | `gregPlugin.AssetExporter`, `gregPlugin.PathRedirector` |
| `gregCore` / `gregCore.<Name>` | core framework, reusable APIs and first-party modules | `gregCore`, `gregCore.Lua` |
| `gregLibs.<Name>` | third-party or adapted dependency distributed through `UserLibs/` | `gregLibs.MoonSharp` |
| `gregTool.<Name>` | developer, mod-management, inspection or repair tool | `gregTool.ModManager`, `gregTool.UnityExplorer` |
| `gregBridge.<Name>` | native, protocol, language or runtime bridge | `gregBridge.Rust` |
| `gregWeb.<Name>` | Greg Framework website, store, wiki, catalog or application | `gregWeb.Modstore`, `gregWeb.LandingWiki` |
| `gregInfra.<Name>` | deployment, build, server or distribution infrastructure dedicated to Greg/Data Center | `gregInfra.Deploy` |
| `gregDocs.<Name>` | standalone documentation or knowledge repository | `gregDocs.DataCenter` |
| `gregResearch.<Name>` | Data Center-specific reverse engineering and reproducible research | `gregResearch.IL2CPP` |
| `gregTheme.<Name>` | Greg-branded external themes and visual integrations | `gregTheme.FrameCord` |

Existing package, assembly, namespace, mod ID and configuration names are migrated separately. A GitHub repository rename must not silently break runtime compatibility.

## 3. Data Center classification test

A repository belongs to the Greg Framework when one or more of the following are true:

1. it targets Data Center assemblies, game APIs, saves, assets or runtime behavior;
2. it installs to Data Center `Mods/`, `Plugins/`, `UserLibs/`, `UserData/` or another game-specific path;
3. it builds, repairs, inspects or generates Data Center IL2CPP/interoperability artifacts;
4. it manages, distributes, documents or hosts Data Center mods and plugins;
5. it provides a Greg Framework API, bridge, compatibility layer or shared dependency;
6. its primary audience is the Data Center modding community.

Generic MelonLoader, Unity or IL2CPP projects are not automatically Greg projects unless their maintained scope is Data Center-specific.

## 4. Required metadata

Every Greg Framework repository adds the following fields to `.meyermedia/repository.yml`:

```yaml
ecosystem: greg-framework
repositoryPrefix: greg
productFamily: data-center # omit only when Greg-branded but not Data Center-specific
canonicalRepository: true
legacyNames: []
```

For consolidated or compatibility repositories:

```yaml
ecosystem: greg-framework
productFamily: data-center
canonicalRepository: false
canonicalTarget: gregMod.IPAM
migrationStatus: consolidating
```

`README.md` and `AGENTS.md` must state:

- that the repository is part of the Greg Framework ecosystem;
- whether it is Data Center-specific;
- its canonical install target or distribution format;
- its canonical successor when deprecated;
- compatibility-sensitive names that must not be changed without migration support.

## 5. Existing Greg-named repositories

All of the following are classified as Greg Framework repositories regardless of their current technical stack:

| Current repository | Canonical category | Planned action |
| --- | --- | --- |
| `gregCore` | core framework | keep as canonical framework root |
| `GregFramework` | legacy framework | consolidate into `gregCore`, then archive |
| `FrikaModFramework` | legacy Data Center framework | consolidate useful APIs into `gregCore` or rename to a scoped `gregCore.*` compatibility module |
| `gregRef` | framework references/API support | keep temporarily; evaluate `gregCore.Ref` during package migration |
| `gregMod.TemplateMod` | mod template | keep as canonical IL2CPP mod template |
| `gregMod.Template` | legacy mod template | consolidate into `gregMod.TemplateMod`, then archive |
| `gregMod.IPAM` | mod | keep canonical |
| `gregIPAM` | legacy mod | consolidate into `gregMod.IPAM`, then archive |
| `gregMod.Inventory` | mod | keep canonical |
| `gregMod.HexViewer` | mod | keep canonical |
| `gregMod.NoEOL` | mod | keep canonical |
| `gregMod.StorageServer` | mod | keep canonical |
| `gregCableRemover` | mod | rename to `gregMod.CableRemover` |
| `gregModGregifyEmployees` | mod | rename to `gregMod.GregifyEmployees` |
| `gregModPathRedirector` | plugin/path integration | rename or consolidate as `gregPlugin.PathRedirector` |
| `gregConsoleInputGuard` | plugin/input integration | rename to `gregPlugin.ConsoleInputGuard` |
| `gregPluginAssetExporter` | plugin | normalize to `gregPlugin.AssetExporter` |
| `gregPluginLangCompatBridge` | plugin/bridge | normalize to `gregPlugin.LangCompatBridge` |
| `gregPluginMultiplayer` | plugin | normalize to `gregPlugin.Multiplayer` |
| `gregPluginPlayerModels` | plugin | normalize to `gregPlugin.PlayerModels` |
| `gregPluginSysadmin` | plugin | normalize to `gregPlugin.Sysadmin` |
| `gregPluginWebUIBridge` | plugin/bridge | normalize to `gregPlugin.WebUIBridge` |
| `gregModmanager` | desktop mod manager | rename to `gregTool.ModManager`; preserve product executable identity until a separate migration is released |
| `gregWeb.Modstore` | web product | keep canonical |
| `gregWeb.LandingWiki` | web/docs product | keep canonical |
| `gregApply` | Greg web product | audit scope; normalize to `gregWeb.Apply` when confirmed |
| `greggorpages` | Greg-branded web content | normalize to `gregWeb.ErrorPages` if it remains part of the ecosystem |
| `GregFrameCord` | Greg-branded Discord theme | normalize to `gregTheme.FrameCord` |

Repository renames should preserve GitHub redirects, update badges and package metadata, and ship compatibility notes before old identifiers are removed.

## 6. Data Center repositories missing the Greg prefix

The following known repositories are Data Center-related and therefore require a Greg-prefixed canonical name or consolidation target:

| Current repository | Proposed canonical name or target | Action |
| --- | --- | --- |
| `RackBuilder` | `gregMod.RackBuilder` | rename and migrate to the canonical mod template |
| `DataCenter-RustBridge` | `gregBridge.Rust` | rename; document FFI and ABI compatibility |
| `dataCenter.UnityExplorer` | `gregTool.UnityExplorer` | rename; retain upstream provenance where applicable |
| `Il2CppAssemblyFixer` | `gregTool.Il2CppAssemblyFixer` | rename if its maintained scope remains Data Center-specific; otherwise split generic upstream logic from Greg adapter code |
| `LuaLoader` | `gregPlugin.LuaLoader` or `gregCore.Lua` | inspect deployment type, then select the plugin or core-module prefix |
| `datacentermods` | `gregWeb.Modstore` | consolidate duplicate web/catalog functionality into the canonical store |
| `DC_MelonRedirect` | `gregPlugin.PathRedirector` | consolidate with `gregModPathRedirector` and archive the duplicate |
| `deploy` | `gregInfra.Deploy` when Data Center-specific | audit contents before rename; split generic deployment code when mixed |
| `src` | scoped `greg*` repository when Data Center-specific | audit, split and rename; generic repository names are prohibited |

Any additional Data Center repository found in future inventory scans must be added to this table and must not remain permanently under an unrelated or generic name.

## 7. Naming rules for new repositories

New Greg/Data Center repositories must:

1. use one canonical prefix from section 2;
2. use PascalCase after the prefix;
3. use a dot to separate the ecosystem/type prefix and product name;
4. avoid abbreviations unless they are established public product terms;
5. avoid generic names such as `src`, `server`, `tools`, `new`, `test` or `deploy` without a scoped prefix;
6. reserve `Template` names for actual GitHub template repositories;
7. avoid encoding versions in repository names;
8. record aliases and replaced repositories in `.meyermedia/repository.yml`.

Preferred examples:

```text
gregMod.RackBuilder
gregPlugin.AssetExporter
gregCore.Networking
gregLibs.MoonSharp
gregTool.ModManager
gregBridge.Rust
gregWeb.Modstore
gregInfra.Release
gregResearch.IL2CPP
```

## 8. Migration sequence

For each rename:

1. classify the repository and determine its canonical prefix;
2. identify package IDs, assemblies, namespaces, configuration keys, URLs and release artifacts that must remain compatible;
3. add `legacyNames` and `canonicalTarget` metadata;
4. update README, AGENTS, badges, CI references and documentation links;
5. rename the GitHub repository;
6. verify GitHub redirects and clone URLs;
7. update dependent repositories through reviewed pull requests;
8. publish migration notes and a compatibility release where necessary;
9. archive duplicates only after downstream references have moved.

Repository naming, runtime identifiers and public package names are separate compatibility surfaces and must be migrated deliberately.