# Shanghai 2026 Pricing Data - JSON Schemas

This directory contains JSON schemas for the Shanghai 2026 pricing data.

## Schema Files

| # | Category | Schema File | Source Files |
|---|----------|-------------|--------------|
| 1 | 水电气 | `1-water-electricity-gas-schema.json` | `1-water-electricity-gas.json` |
| 2 | 公共交通 | `2-public-transport-schema.json` | `2-bus-metro.json` |
| 3 | 出租车与轮渡 | `3-taxi-ferry-schema.json` | `3-taxi-boat.json` |
| 4 | 有线电视与证件 | `4-cable-tv-id-schema.json` | `4-tv-id.json` |
| 5 | 医疗服务 (Part 1) | `5-medical-service-1-schema.json` | `5-medicalservice-1.json` |
| 6 | 医疗服务 (Part 2) | `6-medical-service-2-schema.json` | `6-medicalservice-2.json` |
| 7 | 医疗服务 (Part 3) | `7-medical-service-3-schema.json` | `7-medicalservice-3.json` |
| 8a | 教育培训 (Part 1) | `8-education-1-schema.json` | `8-edu-1.json` |
| 8b | 教育培训 (Part 2) | `8-education-2-schema.json` | `8-edu-2.json` |
| 8c | 教育培训 (Part 3) | `8-education-3-schema.json` | `8-edu-3.json` |
| 8d | 教育培训 (Part 4) | `8-education-4-schema.json` | `8-edu-4.json` |
| 9 | 景区门票 (Part 1) | `9-scenicspots-1-schema.json` | `9-scenicspots-1.json` |
| 10 | 景区门票 (Part 2) | `10-scenicspots-2-schema.json` | `10-scenicspots-2.json` |
| 11 | 景区门票 (Part 3) | `11-scenicspots-3-schema.json` | `11-scenicspots-3.json` |
| 12a | 交通运输 (Part 1) | `12-transportation-1-schema.json` | `12-transportation-1.json` |
| 12b | 交通运输 (Part 2) | `12-transportation-2-schema.json` | `12-transportation-2.json` |
| 12c | 交通运输 (Part 3) | `12-transportation-3-schema.json` | `12-transportation-3.json` |
| 13 | 停车收费 | `13-parking-schema.json` | `13-parking.json` |
| 14 | 不动产登记 | `14-realestate-schema.json` | `14-realestate.json` |

## Total Categories: 10
## Total Schema Files: 17 (19 source files)

## Schema Standards

All schemas follow the JSON Schema Draft 7 specification and include:
- `$schema` declaration
- `title` and `description` fields
- Type definitions with proper constraints
- Enum values where applicable
- Required field specifications
- Nested object and array structures
- String format specifications (e.g., date formats)

## Usage

These schemas can be used for:
- Data validation
- API documentation
- Code generation
- Data migration
- Quality assurance

Example validation with a JSON Schema validator:
```bash
ajv validate -s 1-water-electricity-gas-schema.json -d 1-water-electricity-gas.json
```
