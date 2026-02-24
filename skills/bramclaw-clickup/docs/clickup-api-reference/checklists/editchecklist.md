# Edit Checklist

Rename a task checklist, or reorder a checklist so it appears above or below other checklists on a task. 

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/checklist/{checklist_id}": {
      "put": {
        "summary": "Edit Checklist",
        "tags": [
          "Task Checklists"
        ],
        "description": "Rename a task checklist, or reorder a checklist so it appears above or below other checklists on a task. ",
        "operationId": "EditChecklist",
        "parameters": [
          {
            "name": "checklist_id",
            "in": "path",
            "description": "b8a8-48d8-a0c6-b4200788a683 (uuid)",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "b955c4dc"
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "EditChecklistrequest",
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "position": {
                    "description": "Position refers to the order of appearance of checklists on a task.\\\n \\\nTo set a checklist to appear at the top of the checklists section of a task, use `\"position\": 0`.",
                    "type": "integer",
                    "contentEncoding": "int32"
                  }
                },
                "examples": [
                  {
                    "name": "Updated Checklist",
                    "position": 1
                  }
                ]
              },
              "example": {
                "name": "Updated Checklist",
                "position": 1
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "contentMediaType": "application/json"
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Task Checklists"
    }
  ]
}
```