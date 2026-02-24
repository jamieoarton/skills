# Create Task Attachment

Upload a file to a task as an attachment. Files stored in the cloud cannot be used in this API request.\
 \
***Note:** This request uses multipart/form-data as the content type.*
 \
 ***Tip:** Try our new [V3 Attachments API](ref:postentityattachment), which supports both tasks and File type Custom Fields!*

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
    "/v2/task/{task_id}/attachment": {
      "post": {
        "summary": "Create Task Attachment",
        "tags": [
          "Attachments"
        ],
        "description": "Upload a file to a task as an attachment. Files stored in the cloud cannot be used in this API request.\\\n \\\n***Note:** This request uses multipart/form-data as the content type.*\n \\\n ***Tip:** Try our new [V3 Attachments API](https://developer.clickup.com/reference/postentityattachment), which supports both tasks and File type Custom Fields!*",
        "operationId": "CreateTaskAttachment",
        "parameters": [
          {
            "name": "task_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "9hv"
              ]
            }
          },
          {
            "name": "custom_task_ids",
            "in": "query",
            "description": "If you want to reference a task by its custom task id, this value must be `true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          },
          {
            "name": "team_id",
            "in": "query",
            "description": "When the `custom_task_ids` parameter is set to `true`, the Workspace ID must be provided using the `team_id` parameter.\n \\\nFor example: `custom_task_ids=true&team_id=123`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "multipart/form-data": {
              "schema": {
                "properties": {
                  "attachment": {
                    "type": "array",
                    "items": {}
                  }
                }
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
                  "title": "CreateTaskAttachmentresponse",
                  "required": [
                    "id",
                    "version",
                    "date",
                    "title",
                    "extension",
                    "thumbnail_small",
                    "thumbnail_large",
                    "url"
                  ],
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "version": {
                      "type": "string"
                    },
                    "date": {
                      "type": "integer",
                      "contentEncoding": "int64"
                    },
                    "title": {
                      "type": "string"
                    },
                    "extension": {
                      "type": "string"
                    },
                    "thumbnail_small": {
                      "type": "string"
                    },
                    "thumbnail_large": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    }
                  },
                  "examples": [
                    {
                      "id": "ac434d4e-8b1c-4571-951b-866b6d9f2ee6.png",
                      "version": "0",
                      "date": 1569988578766,
                      "title": "image.png",
                      "extension": "png",
                      "thumbnail_small": "https://attachments-public.clickup.com/ac434d4e-8b1c-4571-951b-866b6d9f2ee6/logo_small.png",
                      "thumbnail_large": "https://attachments-public.clickup.com/ac434d4e-8b1c-4571-951b-866b6d9f2ee6/logo_small.png",
                      "url": "https://attachments-public.clickup.com/ac434d4e-8b1c-4571-951b-866b6d9f2ee6/logo_small.png"
                    }
                  ]
                },
                "example": {
                  "id": "ac434d4e-8b1c-4571-951b-866b6d9f2ee6.png",
                  "version": "0",
                  "date": 1569988578766,
                  "title": "image.png",
                  "extension": "png",
                  "thumbnail_small": "https://attachments-public.clickup.com/ac434d4e-8b1c-4571-951b-866b6d9f2ee6/logo_small.png",
                  "thumbnail_large": "https://attachments-public.clickup.com/ac434d4e-8b1c-4571-951b-866b6d9f2ee6/logo_small.png",
                  "url": "https://attachments-public.clickup.com/ac434d4e-8b1c-4571-951b-866b6d9f2ee6/logo_small.png"
                }
              }
            }
          }
        },
        "deprecated": false
      }
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
      "name": "Attachments"
    }
  ]
}
```